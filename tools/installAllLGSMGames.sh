#!/bin/bash

# run as gameuser

rootDir="/home/gameuser/gameserver"
gamesList="$rootDir/lgsm/data/serverlist.csv"

read -s -p "Root Password:" ROOTPASS || ROOTPASS=''

echo "Updating gameslist cache"
$rootDir/linuxgsm.sh list > /dev/null 2>&1

echo "LinuxGSM adding all games "
while IFS="," read shortName cmdName fullName
do
    echo "$shortName|$cmdName|$fullName"
    $rootDir/linuxgsm.sh $cmdName
    echo $ROOTPASS | su - root $rootDir/$cmdName auto-install
    $rootDir/$cmdName details >> outputDetails.txt
    echo "| $fullName | $shortName | - | " $($rootDir/$cmdName details | grep -i "inbound" | grep -o "[[:digit:]]\{4,5\}")
    echo "| $fullName | $shortName | - | " $($rootDir/$cmdName details | grep -i "inbound" | grep -o "[[:digit:]]\{4,5\}") >> outputREADME.txt
done < $gamesList
