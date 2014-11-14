#!/usr/bin/env python
import sys
import os
import shutil
import subprocess

from os.path import expanduser

if __name__ == '__main__':
    print 'Installing "git-templates"...'

    dest = expanduser('~/.git-templates')

    if os.path.exists(dest):
        answer = raw_input(
            ('%s already exists. '
             'It must be removed to proceed with the installation. Ok [y/N]? ')
            % dest)
        if answer.lower() != 'y':
            print 'Installation terminated'
            sys.exit(0)

        shutil.rmtree(dest)

    shutil.copytree('template', dest)
    print 'Template copied'

    subprocess.check_call(
        'git config --global init.templatedir "%s"' % dest, shell=True)
    print 'git config updated'

    print 'Done! To update existing git repositories run "git init"'
