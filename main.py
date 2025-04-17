import time
import traceback

import pygame

import constants
import gui
import mouse

pygame.init()  # Lance le programme

screen = gui.window()  # Créée une fenêtre

#
print(f"{constants.GAME_NAME} version {constants.GAME_VERSION_FULL}\n(c) 2023 Raindrops, Borterx\n")

grid = [[None for _ in range(3)] for _ in range(3)]  # Définit une grille vide
game = True  # La partie est en train de se jouer
running = True  # Le jeu s'exécute
winner = None  # Il n'y a pas de gagnant
player = "x"  # X est le premier joueur
start = time.time()

try:
    _ui = gui.draw(screen, grid, winner, game, player, start)
    game = _ui[0]
    winner = _ui[1]

    while running:
        if pygame.key.get_pressed()[pygame.K_DELETE]:
            raise Exception("*User initiated crash. Do not report.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                mouse.hover(mouse_position[0], mouse_position[1], grid, player, game, screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                _click = mouse.click(event.pos[0], event.pos[1], grid, player, game, winner)
                grid = _click[0]
                player = _click[1]
                game = _click[2]
                winner = _click[3]

                for k in range(2):  # On exécute ce code 2 fois au cas où "winner" change entre temps
                    _ui = gui.draw(screen, grid, winner, game, player, start)
                    game = _ui[0]
                    winner = _ui[1]
except Exception as e:
    pygame.mixer.music.load("./assets/sounds/crash.wav")
    pygame.mixer.music.play()

    screen.fill((0, 0, 0))

    try:
        img = pygame.image.load("./assets/img/crash.png")
        img.convert()

        rect = img.get_rect()
        rect.x = 302
        rect.y = 197

        screen.blit(img, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, -1)
    except Exception:
        pass

    try:
        message = e.message if hasattr(e, 'message') else str(e)

        if message.startswith("*"):
            code = "0000000F000000003"
        else:
            code = ("".join([hex(ord(i)).split("x")[1] for i in message]) + "0000000000000000").upper()

        screen.blit(pygame.font.Font("./assets/fonts/crash.ttf", 14).render(code[0:8], True, (255, 255, 255)), (282, 242))
        screen.blit(pygame.font.Font("./assets/fonts/crash.ttf", 14).render(code[9:17], True, (255, 255, 255)), (282, 264))

    except Exception:
        pass

    print(traceback.format_exc())
    pygame.display.update()
    pygame.display.set_caption("")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
