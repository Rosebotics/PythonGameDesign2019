#

# My first Pygame program.
# Authors: Many people and Arya

import pygame
import sys
import time

color = (134, 225, 135)

white = (255, 99, 79)
circlelocation = (320, 240)
circleradius = 50

mint =(255, 99, 79)
circlelocation = (325, 245)
circleradius = 50

rectX = 320
rectY = 350
rectWidth = 50
rectHeight =175

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(color)
    pygame.draw.circle(screen, white, circlelocation, circleradius)
    pygame.draw.circle(screen, mint, circlelocation, circleradius)
    pygame.draw.rect(screen,white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()



