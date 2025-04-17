import pygame

import constants
import game
import util
import win

def display_grid(screen):

    # Paramètre une couleur d'arrière-plan
    screen.fill(constants.BG_COLOR)

    # Fond de la grille
    pygame.draw.rect(screen, constants.GAME_COLOR, (20, 20, 440, 440), 0, 5)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (20, 20, 441, 441), 2, 5)

    # Colonne de gauche
    pygame.draw.rect(screen, constants.BORDER_COLOR, (20, 20, 147, 147), 1, 0, 6)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (20, 167, 147, 147), 1)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (20, 314, 147, 147), 1, 0, 0, 0, 6)

    # Colonne du milieu
    pygame.draw.rect(screen, constants.BORDER_COLOR, (167, 20, 147, 147), 1)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (167, 167, 147, 147), 1)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (167, 314, 147, 147), 1)

    # Colonne de droite
    pygame.draw.rect(screen, constants.BORDER_COLOR, (314, 20, 147, 147), 1, 0, 0, 6)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (314, 167, 147, 147), 1)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (314, 314, 147, 147), 1, 0, 0, 0, 0, 6)


def card(screen):
    # Case des informations
    pygame.draw.rect(screen, constants.GAME_COLOR, (480, 141, 140, 200), 0, 5)
    pygame.draw.rect(screen, constants.BORDER_COLOR, (480, 141, 140, 200), 2, 5)


def elements(screen, grid, winner):

    for il in range(len(grid)):
        for ic in range(len(grid[il])):
            if grid[il][ic] is not None:
                factor = 10

                x = 20 + factor if ic == 0 else 167 + factor if ic == 1 else 314 + factor
                y = 20 + factor if il == 0 else 167 + factor if il == 1 else 314 + factor

                # permet de positionner les X et les O sur la grille
                if winner == grid[il][ic]:
                    util.image(x, y, constants.IMG_PLAYER_O_WIN if grid[il][ic] == "o" else constants.IMG_PLAYER_X_WIN,
                               screen)
                else:
                    util.image(x, y, constants.IMG_PLAYER_O if grid[il][ic] == "o" else constants.IMG_PLAYER_X, screen)


def show_version(screen):
    # affiche le nom du jeu ainsi que la version actuelle
    util.text(constants.GAME_NAME, 510, 40, screen, 30, constants.BORDER_COLOR, constants.FONT_FILE)
    util.text(constants.GAME_VERSION, 540, 430, screen, 15, constants.BORDER_COLOR, constants.FONT_FILE)


def window():
    screen = pygame.display.set_mode((640, 480), vsync=1)  # Définit la taille de la fenêtre

    # mets les informations du jeu dans le nom de la fenêtre
    pygame.display.set_caption(
        f"{constants.GAME_NAME} v{constants.GAME_VERSION_FULL} - pygame {pygame.version.ver}, SDL {pygame.version.SDL[0]}.{pygame.version.SDL[1]}.{pygame.version.SDL[2]}")  # Permet de mettre le nom de la fenêtre
    pygame.display.set_icon(pygame.image.load(constants.IMG_GAME_ICON))

    return screen


def draw(screen, grid, winner, playing, player, start):
    # permet de lancer le, avec toutes les valeurs
    display_grid(screen)
    card(screen)
    elements(screen, grid, winner)
    show_version(screen)
    game.show_restart(screen)

    if playing:
        # si la manche est en cours
        game.show_player(screen, player)
        _win = win.winning(winner, playing, grid, start)
        playing = _win[0]
        winner = _win[1]

        if not playing:
            # si la manche n'est pas en cours, c'est-à-dire que la manche est terminée
            util.sound(constants.SOUND_FINISH)
    else:
         # affiche le gagnant de la manche
        win.show_winner(screen, winner)

    pygame.display.update()
    return playing, winner
