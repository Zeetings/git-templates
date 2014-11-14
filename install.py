#!/usr/bin/env python
import sys
import os
import shutil
import subprocess

from os.path import expanduser


DEFAULT_CONFIG_CMDS = [
    # Rebase when pulling new branches
    'branch.autosetuprebase always',
    # Rebase when pulling 'master'
    'branch.master.rebase true',
    # Rebase when pulling 'dev'
    'branch.dev.rebase true',
    # Push only the branch you are on
    'push.default simple',

    # Color highlighting
    'color.ui true',
    'color.status auto',
    'color.branch auto'
]

DEFAULT_ALIASES = [
    # List your git aliases. Because sometimes you don't remember your aliases.
    'la "!git config -l | grep alias | cut -c 7-"',
    # Short and sweet status
    'st "status -sb"',
    # Review git history like a pro
    'tree "log --graph --oneline --decorate --abbrev-commit"',
    # Because we all commit mistakes
    'undo "reset --soft HEAD^"',
    # List the last branches you've been working on by modification date order
    'lastbranches "git for-each-ref --sort=-committerdate refs/heads | cut -c60- | head"'
    # Remove merged branches as long as they are not 'master' or 'dev'
    'prunebranches "git branch --merged dev | grep -v \'master$\' | grep -v \'dev$\' | xargs git branch -d"',
    # Displays the log listing affected files per commit
    'lsv "log --pretty=format:\'%C(yellow)%h %C(blue)%ad%C(red)%d %C(reset)%s%C(green) [%cn]\' --decorate --date=short --numstat"',
    # Flat and colorful way of seeing your history
    'ls "log --pretty=format:\'%C(yellow)%h %C(blue)%ad%C(red)%d %C(reset)%s%C(green) [%cn]\' --decorate --date=short"',
    # Diff against the index
    'dc "diff --cached"',
    # Ignore spaces and tabs
    'diff "diff --word-diff"',
    'listtags "log --tags --simplify-by-decoration --pretty=\'format:%ai %d\'"',
]


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

    # Set up git templates dir
    subprocess.check_call(
        'git config --global init.templatedir "%s"' % dest, shell=True)
    print 'git config updated'

    # Update default config options
    for cmd in DEFAULT_CONFIG_CMDS:
        subprocess.check_call('git config --global %s' % cmd, shell=True)
    # Update default aliases
    for alias in DEFAULT_ALIASES:
        subprocess.check_call(
            'git config --global alias.%s' % alias, shell=True)
    print ('Global git configuration updated. '
           'Run "git config --global --list" to see the changes.')

    print 'Done! To update existing git repositories run "git init"'
