from os         import path
from fabric.api import env, sudo, put

env.use_ssh_config = True

def nginx_put_repofile():
    repofile = path.dirname(path.abspath(__file__)) + '/repofile/nginx.centos.repo'
    put(repofile, '/tmp')
    sudo('install -v -o root -g root -m 0644 /tmp/nginx.centos.repo /etc/yum.repos.d/nginx.repo')

def nginx_install():
    sudo('yum -y install nginx')
