import signal
import time
import sys
import os
from shutil import copy

def main(games_dir):
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    games_list = next(os.walk(games_dir))[1]
    games = []
    for dir in games_list:
        with open(os.path.join(games_dir, dir, "game_properties.sh")) as props:
            for line in props:
                if line.startswith('GAME_LONG_NAME'):
                    _, full_name = line.strip().split('=', 1)
                    if full_name.startswith('"') and full_name.endswith('"'):
                        full_name = full_name[1:-1]
                    games.append((dir, full_name))
                    break
    
    from dialog import Dialog
    d = Dialog(dialog="dialog")
    choices = [(str(i)+")",game[1]) for i,game in enumerate(games)]
    _, gamenum = d.menu("Choose a game to install:",
                        title="Game Server Installer",
                        choices=choices,
                        no_cancel=True)
    selected_index = int(gamenum[0:-1])
    selected_game = games[selected_index]
    copy(os.path.join(games_dir, selected_game[0], "game_properties.sh"), "/etc/gameserver/gameserver")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide path to gameservers directory")
        exit(1)
    main(sys.argv[1])
