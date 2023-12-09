#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime

env.hosts = ['3.85.196.229', '34.207.221.84']


def do_pack():
    local("mkdir -p versions")
    created = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(created))
    return ("versions/web_static_{}.tgz".format(created))


def do_deploy(archive_path):
    if not archive_path:
        return False

    put(archive_path, "/tmp/")
    file_name = archive_path.split("/")[-1]
    no_ext = file_name.split(".")[0]
    run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
    run("tar -xzf /tmp/{} -C /data/web_statsic/release/{}/".format(file_name, no_ext))
    run("rm /tmp/{}".format(file_name))
    run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(no_ext, no_ext))
    run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))
    print("New version deployed!")


def deploy():
    """
    Creates & Distributes an archive to the web servers.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
