#!/bin/bash

rootDir="/home/gameuser/gameserver/"
gamesList="$rootDir/lgsm/data/serverlist.csv"

echo "Updating gameslist cache"
sudo -u gameuser $rootDir/linuxgsm.sh list > /dev/null 2>&1

echo "Generating games list"
while IFS="," read shortName cmdName fullName
do
  gameDir="/root/linux-gameservers/games/$shortName"
  mkdir -p "$gameDir"
  if [ ! -f "$gameDir/game_properties.sh" ]; then
    echo "$shortName|$cmdName|$fullName"
    echo -e "GAME=\""$shortName"\"\nGAME_LONG_NAME=\""$fullName"\""
    echo -e "GAME=\""$shortName"\"\nGAME_LONG_NAME=\""$fullName"\"" > "$gameDir/game_properties.sh"
  fi
done < $gamesList
