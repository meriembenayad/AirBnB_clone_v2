#!/usr/bin/python3
""" Fabric script that generates a .tgz archive and deploys it to web servers """
from fabric.api import local, put, run, env
from datetime import datetime
from os import path, mkdir
# Import do_pack from 1-pack_web_static file
from pack_web_static import do_pack

env.hosts = ['3.85.196.229', '34.207.221.84']


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
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(dir_release))
        return True
    except FileNotFoundError:
        return False
