#!/usr/bin/python3
"""script to zip folder"""
import datetime
from fabric.api import local
from os.path import isdir


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
