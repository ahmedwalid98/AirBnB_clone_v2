#!/usr/bin/python3
"""
    deploy arvhice
"""
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['100.26.211.99', '54.80.43.239']


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
