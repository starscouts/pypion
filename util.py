import time

import pygame

import constants


def text(message, x, y, screen, size, color, font):
    # permet d'afficher du texte
    screen.blit(pygame.font.Font(font, size).render(message, True, color), (x, y))


def image(x, y, filename, screen):
    # permet d'afficher une image
    img = pygame.image.load(filename)
    img.convert()

    rect = img.get_rect()
    rect.x = x
    rect.y = y

    screen.blit(img, rect)
    pygame.draw.rect(screen, constants.BG_COLOR, rect, -1)


def log(message):
    # permet d'afficher les événements réalisés dans la console
    date = time.ctime()
    print(f"[{date}] {message}")


def sound(filename):
    # permet de jouer un son
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(filename))