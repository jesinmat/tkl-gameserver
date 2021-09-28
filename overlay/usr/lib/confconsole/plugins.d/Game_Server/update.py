'''Update LinuxGameservers management software'''
import os
import subprocess

GAME_REPO_DIR="/root/gameservers"
GAME_REPO_URL="https://github.com/jesinmat/linux-gameservers.git"

def is_update_available():
    ret = subprocess.run(
            ['git', 'ls-remote', 'origin', 'refs/heads/master'],
            capture_output=True, text=True)
    if ret.returncode != 0:
        return ('error', ret.stderr)

    # get first line of output, split by spaces (should be a commit id of
    # remote head)
    remote_head = ret.stdout.splitlines()[0].strip().split()[0]

    ret = subprocess.run(['git', 'rev-parse', 'HEAD'],
            capture_output=True, text=True)
    if ret.returncode != 0:
        return ('error', ret.stderr)

    local_head = ret.stdout.splitlines()[0].strip()
    return ('ok', local_head != remote_head)

def run():
    curdir = os.getcwd()
    os.chdir(GAME_REPO_DIR)

    ok, data = is_update_available()
    if ok == 'error':
        console.msgbox('Error',
                'An error occured checking for updates:\n',
                data)
        os.chdir(curdir)
        return

    if data:
        console.infobox('Updates found, performing updates...')
        ret = subprocess.run(['git', 'pull'], capture_output=True, text=True) 

        if ret.returncode != 0:
            console.msgbox('Error',
                    'An error occured during update:\n',
                    ret.stderr)
        else:
            console.msgbox('Update', 'Update success')
    else:
        console.msgbox('Updates', 'No updates found')
    os.chdir(curdir)
