import signal
import time
import sys
import os
from shutil import copy


def parse_games_from_directory(games_dir):
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
    return games


def show_dialog(games):
    from dialog import Dialog
    d = Dialog(dialog="dialog")
    games.sort(key=lambda game: game[1])
    choices = [(str(i)+")", game[1]) for i, game in enumerate(games)]
    _, gamenum = d.menu("Choose a game to install:",
                        title="Game Server Installer",
                        choices=choices)
    if gamenum:
        return games[int(gamenum[0:-1])]
    return None


def main(gameservers_dir):
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    games_dir = os.path.join(gameservers_dir, "games")
    games = parse_games_from_directory(games_dir)
    selected_game = show_dialog(games)
    if selected_game:
        copy(os.path.join(games_dir, selected_game[0], "game_properties.sh"),
             "/etc/gameserver/gameserver")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide path to gameservers repository directory!")
        exit(1)
    main(sys.argv[1])
