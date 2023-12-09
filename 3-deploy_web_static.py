#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime

env.hosts = ['3.85.196.229', '34.207.221.84']

@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")
    created = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(created))
    return ("versions/web_static_{}.tgz".format(created))


def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Parameters:
    archive_path (str): The path to the archive

    Returns:
    bool: True if all operations were successful, False otherwise
    """

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Get the base name, file name, dest of the archive
        base_name = archive_path.split("/")[-1]
        file_name = base_name.split(".")[0]
        dest_path = "/data/web_static/releases/{}/".format(file_name)

        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(dest_path))
        run("tar -xzf /tmp/{} -C {}".format(base_name, dest_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(base_name))

        # Move the files
        run("mv {0}web_static/* {0}".format(dest_path))

        # Delete the symbolic link from the web server
        run("rm -rf {}web_static".format(dest_path))
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link on the web server
        run("ln -s {} /data/web_static/current".format(dest_path))

        # TADA
        print("New version deployed!")

    except Exception:
        return False

    return True


def deploy():
    """Creates and distributes an archive to your web servers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
