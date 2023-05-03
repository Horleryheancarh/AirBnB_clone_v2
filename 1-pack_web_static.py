#!/usr/bin/python3
""" Function to compress folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        time = datetime.now()
        fmt = '%Y%m%d%H%M%S'
        arc = 'versions/web_static_{}.tgz'.format(time.strftime(fmt))
        local('tar -zcvf {} web_static'.format(arc))
        return arc
    except:
        return None
