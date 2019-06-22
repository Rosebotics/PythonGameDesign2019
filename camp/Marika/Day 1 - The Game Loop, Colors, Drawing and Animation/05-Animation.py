# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# My first Pygame program.
# Authors: Many people and Marika

import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (140, 100, 255)
rectColor = (255, 100, 100)
circleRadius =  20

rectY = 100
rectSpeed = 5
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((backgroundColor))

    rectY = rectY + rectSpeed
    if rectY > 405:
        rectSpeed = -5
    elif rectY < 0:
        rectSpeed = 5


    pygame.draw.circle(screen, (circleColor), (320, 150), circleRadius)
    pygame.draw.rect(screen, (rectColor), (600, rectY, 20, 75))


    pygame.display.update()
