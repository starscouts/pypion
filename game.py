import constants
import util


def show_player(screen, player):
    # permet d'afficher le joueur en cours (X ou O)
    util.text(constants.LANG_PLAYER, 508, 151, screen, 30, constants.BORDER_COLOR, constants.FONT_FILE)
    util.image(485, 200, constants.IMG_PLAYER_O if player == "o" else constants.IMG_PLAYER_X, screen)


def place(line, col, grid, player, game):
    # si le jeu n'est pas en cours, alors rien ne se passe rien
    if not game:
        return grid, player

    # si la case est vide, alors cela met la croix ou le cercle sur la grille
    if grid[line][col] is None:
        grid[line][col] = player
        player = "o" if player == "x" else "x"
        util.sound(constants.SOUND_CLICK)
    else:
        util.sound(constants.SOUND_NO) # on joue le son "Non" car la case est déjà prise

    return grid, player


def show_restart(screen):
    # affiche le bouton permettant de relancer le jeu
    util.image(481, 348, constants.IMG_RESTART, screen)


def restart():
    # permet de redémarrer le jeu, en jouant un son et en remettant les valeurs par défaut
    util.sound(constants.SOUND_CLICK)

    game = True
    player = "x"
    grid = [[None for _ in range(3)] for _ in range(3)]
    winner = None

    return grid, player, game, winner
