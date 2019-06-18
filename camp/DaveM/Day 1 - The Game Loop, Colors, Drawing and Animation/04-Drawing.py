# My first Pygame program.
# Authors: Many people and Bilbo

import pygame
import sys

backgroundColor = (255, 255, 100)

white = (255, 255, 255)
circleLocation = (300, 150)
circleRadius = 20

rectX = 600
rectY = 100
rectWidth = 20
rectHeight = 75


pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circleLocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()



