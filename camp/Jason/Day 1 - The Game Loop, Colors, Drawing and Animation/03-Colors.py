# My first Pygame program.
# Authors: Many people and Jason <PUT-YOUR-NAME-HERE>

import pygame
import sys
import time

backgroundColor = (0, 110, 110)
pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    pygame.display.update()

