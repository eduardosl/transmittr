# Automation workflow for deployment
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm


USERNAME = 'root'
SERVER = '192.168.1.2'
APP_NAME = 'transmittr'
#PROJECT_DIR = '/www/%s/%s' % (SERVER, APP_NAME)
PROJECT_DIR = '~/%s' % APP_NAME
WSGI_SCRIPT = 'app.wsgi'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prepare_deploy():
    commit()
    push()

def deploy():
    with settings(warn_only=True):
        if run("test -d %s" % PROJECT_DIR).failed:
            run("git clone https://github.com/eduardosl/transmittr.git %s" % PROJECT_DIR)
    with cd(PROJECT_DIR):
        run('git pull')
        #run('bin source/activate') # virtualenv on the beaglebone is broken...
        run('pip install -r requirements.txt')
        run('chmod +x logger_startup.sh')
        run('./logger_startup.sh')
        run('touch %s' % WSGI_SCRIPT)
