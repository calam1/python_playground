#!/usr/bin/env python
from fabric.api import local, settings
from distutils.version import LooseVersion

def version():
    with settings():
        installed_chef_version = local('chef-solo -version | grep -Eo "([0-9]+\.[0-9]+\.[0-9]+)"', capture=True)
        is_greater_than_min_version = LooseVersion(installed_chef_version) > LooseVersion("12.6.0")
        print 'Installed Chef version is %s' % (installed_chef_version)
        print 'Installed Chef version is greater than 12.6.0 %s' % (is_greater_than_min_version)

