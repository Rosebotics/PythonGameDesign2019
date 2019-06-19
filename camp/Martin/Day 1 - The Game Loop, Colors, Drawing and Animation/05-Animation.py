# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.



# My first Pygame program.
# Authors: Martin W.

import pygame
import sys
import time

backgroundColor = (0, 0, 255)

Red = (255, 0, 0)
circleLocation = (320, 240)
circleRadius = 200
width = 199

Yellow = (255, 255, 0)
rectX = 260
rectY = 220
rectWidth = 120
rectHeight = 40


rect2X = 280
rect2Y = 230
rect2Width = 80
rect2Height = 20

RectSpeed = 1
CircleSpeed = 1

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)

    circleRadius = circleRadius + 1
    rectWidth = rectWidth + 2
    rectHeight = rectHeight + 2
    rectX = rectX - 1
    rectY = rectY - 1
    rect2Width = rect2Width + 2
    rect2Height = rect2Height + 2
    rect2X = rect2X - 1
    rect2Y = rect2Y - 1

    pygame.draw.circle(screen, Red, circleLocation, circleRadius, width)
    pygame.draw.rect(screen, Yellow, (rectX, rectY, rectWidth, rectHeight))
    pygame.draw.rect(screen, backgroundColor, (rect2X, rect2Y, rect2Width, rect2Height))
    pygame.display.update()









