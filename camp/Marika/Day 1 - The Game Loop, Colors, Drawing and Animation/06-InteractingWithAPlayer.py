# My first Pygame program.
# Authors: Many people and Marika

import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (140, 100, 255)
rectColor1 = (255, 100, 120)
rectColor2 = (100, 120, 255)
circleRadius =  20

rectY1 = 100
rectY2 = 100
rectSpeed = 5
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY1 = rectY1 - 5
        if pressed_keys[K_DOWN]:
            rectY1 = rectY1 + 5
        if pressed_keys[K_w]
            rectY2 = rectY2 -5
        if pressed_keys[K_s]


    screen.fill((backgroundColor))



    pygame.draw.circle(screen, (circleColor), (320, 150), circleRadius)
    pygame.draw.rect(screen, (rectColor1), (600, rectY1, 20, 75))
    pygame.draw.rect(screen, (rectColor2), (30, rectY2, 20, 75))


    pygame.display.update()

