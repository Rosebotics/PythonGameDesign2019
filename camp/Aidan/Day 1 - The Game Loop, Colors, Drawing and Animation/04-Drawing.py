
# My first Pygame program.
# Authors: Many people and Aidan

import pygame
import sys

backgroundColor = (50, 60, 123.456789)
white = (255, 255, 255)
circleLocation = (300, 150)
circleRaidous = 200
circleLocation = (300, 150)
circleRaidous = 35
red = (255, 255, 255)
pygame.init()

screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circleLocation, circleRaidous)
    pygame.draw.circle(screen, white, circleLocation, circleRaidous)
    pygame.display.update()


