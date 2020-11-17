#!/usr/bin/python3
"""Set Gameserver Repo and Branch

Options:
    --gameserver-repo=      unless provided, will ask interactively
    --gameserver-branch=    unless provided, will ask interactively

"""
import os
import sys
import getopt
import subprocess
from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print('Syntax: %s [options]' % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'h',
                ['help', 'gameserver-repo=', 'gameserver-branch='])
    except getopt.GetoptError as e:
        usage(e)

    default_gameserver_repo = 'https://github.com/jesinmat/linux-gameservers.git'
    default_gameserver_branch = 'master'

    gameserver_repo = ""
    gameserver_branch = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--gameserver-repo':
            gameserver_repo = val
        elif opt == '--gameserver-branch':
            gameserver_branch = val

    dialog = Dialog('TurnKey Linux - First boot configuration')

    if not gameserver_repo or not gameserver_branch:
        choose_gameserver_upstream = dialog.yesno(
                'TKL Gameserver',
                'Do you want to choose a custom repo?')
        if choose_gameserver_upstream:
            if not gameserver_repo:
                ok, gameserver_repo = dialog.inputbox(
                    'TKL Gameserver',
                    'Choose gameserver repo url',
                    default_gameserver_repo)
                if not ok:
                    gameserver_repo = default_gameserver_repo
            if not gameserver_branch:
                ok, gameserver_branch = dialog.inputbox(
                    'TKL Gameserver',
                    'Choose gameserver branch',
                    default_gameserver_branch)
                if not ok:
                    gameserver_branch = default_gameserver_branch

        else:
            gameserver_repo = default_gameserver_repo
            gameserver_branch = default_gameserver_branch

    needs_pull = False
    old_dir = os.getcwd()
    if gameserver_repo != default_gameserver_repo:
        os.chdir('/root/gameservers')
        subprocess.run([
            'git', 'remote', 'set-url', 'origin',
            gameserver_repo
        ])
        needs_pull = True
    if gameserver_branch != default_gameserver_branch:
        os.chdir('/root/gameservers')
        subprocess.run([
            'git', 'fetch'
        ])
        subprocess.run([
            'git', 'checkout', '--track',
            f'origin/{gameserver_branch}',
        ])
        needs_pull = True

    if needs_pull:
        os.chdir('/root/gameservers')
        subprocess.run([
            'git', 'pull'
        ])
        
    os.chdir(old_dir)

if __name__ == '__main__':
    main()
