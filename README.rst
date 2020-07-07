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

Headless installation
---------------------

User data can be passed to the image before the first boot. Cloud service providers offer ways to run
scripts before launching the instance, enabling the user to set the environment.
You can use `supported environment variables`_ from Linux Gameservers to initialize your game server without
user interaction.

Below is a sample init script.

.. code-block:: console
    :linenos:
    #!/bin/bash

    cat>/etc/inithooks.conf<<EOF
    export ROOT_PASS=YourSecretRootPassword
    export DB_PASS=YourSecretMysqlPassword
    export APP_PASS=YourSecretWebappPassword
    export APP_EMAIL=admin@example.com
    export HUB_APIKEY=SKIP
    export SEC_UPDATES=FORCE

    export GAME="mc"
    export GAME_SERVER_NAME="My first game server"
    EOF

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, Shellinabox: username **root**
-  Game server: username **gameuser** (if you need to log in as this user, connect as root and switch users)

.. _TurnKey GNU/Linux: https://www.turnkeylinux.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Linux Gameservers: https://github.com/jesinmat/linux-gameservers
.. _LinuxGSM: https://linuxgsm.com/
.. _supported environment variables: https://github.com/jesinmat/linux-gameservers#supported-games
