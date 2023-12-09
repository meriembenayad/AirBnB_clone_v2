#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
and deploys it to web servers
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os import path, mkdir

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<your-ssh-username>'
env.key_filename = '<path-to-your-ssh-private-key>'


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
        # The directory where the archive should be uncompressed
        dir_release = "/data/web_static/releases/{}".format(name)
        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(dir_release))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_release))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))
        # Move extraction to the proper directory
        run('mv {0}/web_static/* {0}/'.format(dir_release))
        # Delete the first copy of extraction after move
        run('rm -rf {}/web_static'.format(dir_release))
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(dir_release))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Deploys the web_static content to web servers.
    """
    # Call the do_pack() function and store the path of the created archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if not archive_path:
        return False

    try:
        # Call the do_deploy(archive_path) function using the new path of the new archive
        result = do_deploy(archive_path)

        # Return the return value of do_deploy
        return result
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
