#!/usr/bin/python3
""" Function to compress folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ Pack Files """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        time = datetime.now()
        fmt = '%Y%m%d%H%M%S'
        arc = 'versions/web_static_{}.tgz'.format(time.strftime(fmt))
        local('tar -zcvf {} web_static'.format(arc))
        size = os.stat(arc).st_size
        print('web_static packed: {} -> {}Bytes'.format(arc, size))
        return arc
    except:
        return None
