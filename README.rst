GameServer - Host your own game server
=======================================================

GameServer is a `TurnKey GNU/Linux`_ appliance for hosting
game servers on Linux. It provides a way of deploying game servers
in minutes in cloud environments.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Managing game servers using `Linux Gameservers`_:
    - Downloads newest version during first boot to ensure best possible game support
    - Wrapper for `LinuxGSM`_ with support for up to 100 games

- Fully automatic or interactive game server selection:
    - All required settings can be passed via user data, game server starts within minutes
    - If no data is provided, graphical interface will prompt user to select required game server

Usage
-----

Interactive installation
^^^^^^^^^^^^^^^^^^^^^^^^

When running this appliance with an interactive output (such as in a local virtual machine),
you will be guided through the game server installation using a graphical interface.

During the installation, you will be asked to provide basic server settings for the game server.

Manual headless installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're launching this appliance in a cloud environment without providing user data (see next chapter for details about user data),
you will need to log into the server using SSH and start the game server installation either in the Configuration Console menu (``confconsole``) or by using the ``gameserver-init`` command. A graphical interface will guide you through the installation.

Automatic headless installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User data can be passed to the image before the first boot. Cloud service providers offer ways to run
scripts before launching the instance, enabling the user to set the environment.
You can use `supported environment variables`_ from Linux Gameservers to initialize your game server without
user interaction. Password for the **gameuser** account can be set through the ``APP_PASS`` variable.

Below is a sample init script::

    #!/bin/bash

    cat>/etc/inithooks.conf<<EOF
    export ROOT_PASS=YourSecretRootPassword
    export DB_PASS=YourSecretMysqlPassword
    export APP_PASS=YourSecretWebappAndGameuserPassword
    export APP_EMAIL=admin@example.com
    export HUB_APIKEY=SKIP
    export SEC_UPDATES=FORCE

    export GAME="mc"
    export GAME_SERVER_NAME="My first Minecraft game server"
    EOF

In case you don't specify the ``GAME`` variable, you can choose a game server later by logging into the appliance and following the guide in `Manual headless installation`_.

Logs
^^^^

Game server installation logs are stored in ``/var/log/gameserver/install.log``.
Other game server logs, as well as the server itself, are stored in ``/home/gameuser/gameserver/``.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, Shellinabox: username **root**
-  Game server: username **gameuser**

.. _TurnKey GNU/Linux: https://www.turnkeylinux.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Linux Gameservers: https://github.com/jesinmat/linux-gameservers
.. _LinuxGSM: https://linuxgsm.com/
.. _supported environment variables: https://github.com/jesinmat/linux-gameservers#supported-games
