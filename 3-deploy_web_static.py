#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
"""
from fabric.api import local, put, run, env, runs_once, task
from datetime import datetime
from os import path, mkdir

env.hosts = ['3.85.196.229', '34.207.221.84']


@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Get the current date and time in the format YYYYMMDDHHMMSS
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the path of the archive file to be created
    file_path = "versions/web_static_{}.tgz".format(date)

    # Check if the versions directory exists, if not create it
    if not path.exists("versions"):
        mkdir("versions")

    # Use local command to create .tgz archive of web_static directory
    local("tar -cvzf {} web_static".format(file_path))

    # Check if the archive was created successfully
    if path.exists(file_path):
        return file_path
    else:
        return None


@task
def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Get the file name without extension
        file_name = archive_path.split("/")[-1]
        name = file_name.split('.')[0]
        # The directory where the archive should be uncompress
        dir_release = "/data/web_static/releases/{}".format(name)
        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(dir_release))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_release))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))
        # Move extraction to proper directory
        run('mv {0}/web_static/* {0}/'.format(dir_release))
        # Delete first copy of extraction after move
        run('rm -rf {}/web_static'.format(dir_release))
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(dir_release))
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False


@task
def deploy():
    """
    Creates & Distributes an archive to the web servers.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
