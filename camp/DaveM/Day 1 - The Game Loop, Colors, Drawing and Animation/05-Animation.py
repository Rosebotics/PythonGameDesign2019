# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# My first Pygame program.
# Authors: Many people and Bilbo

import pygame
import sys
import time

backgroundColor = (255, 255, 100)

white = (255, 255, 255)
circleLocation = (300, 150)
circleRadius = 20

rectX = 600
rectY = 100
rectWidth = 20
rectHeight = 75

rectSpeed = 1
circleSpeed = 1
circleX = 300
circleY = 200

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    time.sleep(0.05)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)

    #circleRadius = circleRadius + 1
    circleX = circleX + 1

    pygame.draw.circle(screen, white, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()




