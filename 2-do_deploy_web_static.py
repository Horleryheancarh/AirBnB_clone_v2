#!/usr/bin/python3
""" Function to compress folder """
from fabric.api import *
import shlex
import os


env.hosts = ['18.234.192.243', '35.174.211.240']


def do_deploy(archive_path):
    """ Deploy """
    if not os.path.exists(archive_path):
        return False
    try:
        print(archive_path)

        allname = archive_path.replace('/', ' ')
        allname = shlex.split(allname)
        allname = allname[-1]
        fname = allname.replace('.', ' ')
        fname = shlex.split(fname)
        fname = fname[0]

        print("allname: ", allname, " fname: ",fname)

        releases_path = '/data/web_static/releases/{}/'.format(fname)
        temp = '/tmp/{}'.format(allname)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf {} -C {}'.format(temp, releases_path))
        run('rm {}'.format(temp))
        run('mv {}web_static/* {}'.format(releases_path, releases_path))
        run('rm -rf {}web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except:
        return False
