# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and Henry

import pygame
import sys
from pygame.locals import *

screensize = (640, 480)
backgroundColor = (255, 220, 100)
circleColor =  (0, 0, 0)
circleRadius = 20
rectColor = (255, 255, 255)

rectY = 100
rectSpeed = 20

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY - rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed


    #fill background before drawing
    
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor , (300, 150), circleRadius)
    pygame.draw.rect(screen, (rectColor), (600, rectY, 20, 75))

    pygame.display.update()
