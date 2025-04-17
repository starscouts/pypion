import os
import time

import constants
import util

if not os.path.isdir(constants.DATA_FOLDER):
    # on ajoute le dossier data s'il n'existe pas encore
    os.mkdir(constants.DATA_FOLDER)

if not os.path.isfile(constants.DATA_GAMES):
    # on ajoute le fichier "games.csv" s'il n'existe pas encore
    file = open(constants.DATA_GAMES, "a")
    file.write(f"{';'.join(constants.LANG_TABLE)}\n")
    file.close()


def save(grid, winner, start):
    # permet de sauvegarder les données du jeu
    loser = None
    count = 0

    if winner == 'x':
        loser = 'o'
    elif winner == 'o':
        loser = 'x'

    # le compteur indique le nombre de manches jouées
    for i in grid:
        for j in i:

            if j is not None:
                count += 1

    # calcule le temps qui s'est écoulé entre le lancement et la fin de la manche
    end = time.time()
    game_time = round(end - start)
    time_text = f"{game_time} {constants.LANG_SECONDS}"

    # si ce temps est plus grand qu'une minute, alors on affiche les minutes et les secondes écoulées
    if game_time > 60:
        time_text = f"{round(game_time / 60)}  {constants.LANG_MINUTES}, {game_time - (round(game_time / 60) * 60)}  {constants.LANG_SECONDS}"

    # on enregistre les données dans le fichier "games.csv"
    f = open(constants.DATA_GAMES, "a")
    f.write(
        f"{winner if winner is not None else '-'};{loser if winner is not None else '-'};{constants.LANG_YES if winner is None else constants.LANG_NO};{count};{time_text}\n")
    f.close()
    util.log(f"Game data saved to {constants.DATA_GAMES}")
