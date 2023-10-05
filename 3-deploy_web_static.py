#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.26.211.99', '54.80.43.239']


def do_pack():
    """zipping folder"""
    try:
        if not isdir('versions'):
            local("mkdir -p versions")
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """
        deploy on server
    """
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split('/')[-1]
        no_exten = file.split('.')[0]
        dirc = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(dirc, no_exten))
        run('tar -xzf /tmp/web_static_20231005184742.tgz -C {}{}/'
            .format(dirc, no_exten))
        run('rm /tmp/{}.tgz'.format(no_exten))
        run('mv {}{}/web_static/* {}{}/'
            .format(dirc, no_exten, dirc, no_exten))
        run('rm -rf {}{}/web_static'.format(dirc, no_exten))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(dirc, no_exten))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
