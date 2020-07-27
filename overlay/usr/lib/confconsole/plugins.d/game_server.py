'''Select and install a gameserver'''
import os

def run():
        if os.path.exists('/etc/gameserver/installation.done'):
                console.msgbox('Info', 'Game Server is already installed.')
                return

        console.msgbox('Game Server Installer', 'Before you install a game server, new user account will be created for this purpose. '
                       'Select a secure password for this account on the next screen. '
                       'Do not select the same password as for the root account.\n\n'
                       'Some game servers require basic configuration, such as setting the server name. '
                       'You might be prompted for this info during the installation.')
        os.system('gameserver-init')
        console.msgbox('Info', 'Game Server was successfully installed.'
                               'You can connect to this server using the IP address shown in the configuration console.')
