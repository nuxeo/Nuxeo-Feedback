#!/usr/bin/env python

from fabric.api import *
from fabric.contrib.console import confirm
import os, time

env.hosts = ['root@styx.nuxeo.com']

def pack():
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    local("tar czf tmp/nuxeo-feedback.tgz "
      "--exclude feedback.db --exclude tmp --exclude .git --exclude env "
      '.')

def deploy():
    pack()
    put('tmp/nuxeo-feedback.tgz', '/tmp/')
    with cd('/var/www/nuxeo-feedback'):
        run("cp feedback.db ../feedback.db-%d" % int(time.time()))
        run('tar xzf /tmp/nuxeo-feedback.tgz')
        run("make env")
        run('mv settings-prod.cfg settings.cfg')
        run('touch /var/www/wsgi-scripts/feedback.wsgi')