
# My first Pygame program.
# Authors: Many people and Aidan

import pygame
import sys
import time

backgroundColor = (50, 60, 123.456789)

white = (255, 255, 255)
circleLocation = (300, 150)
pygame.init()

circleRaidous = 100



rectSpeed = 1
screen = pygame.display.set_mode((640, 480))
while True:
    time.sleep(0.09)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    circleRaidous = circleRaidous + 1
    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circleLocation, circleRaidous)


    pygame.display.update()


# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
