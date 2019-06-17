

# My first Pygame program.
# Authors: Martin W.

import pygame
import sys

backgroundColor = (0, 0, 255)

red = (255, 0, 0)
circleLocation = (320, 240)
circleRadius = 300
width = 299

green = (0, 255, 0)
rectX = 310
rectY = 204
rectWidth = 20
rectHeight = 75

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, red, circleLocation, circleRadius, width)
    pygame.draw.rect(screen, green, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()









