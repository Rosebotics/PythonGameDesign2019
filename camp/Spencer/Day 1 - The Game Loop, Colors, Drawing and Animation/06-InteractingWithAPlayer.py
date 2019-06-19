# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and Spencer

import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (255, 255, 255)
circlePos = (320, 230)
rectY = 100
rectSpeed= 20
circleY = 230




pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY= rectY -rectSpeed
        if pressed_keys[K_DOWN]:
            rectY= rectY + rectSpeed

    screen.fill(backgroundColor)


    print(rectY)
    pygame.draw.circle(screen, (circleColor), (circlePos), 15)
    pygame.draw.rect(screen, (circleColor), (600, rectY, 15, 75))
    pygame.draw.rect(screen, (circleColor), (40, rectY, -15, 75))
    pygame.display.update()

