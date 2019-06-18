import pygame
import sys
from pygame.locals import *

screensize = (640, 480)
backgroundcolor = (255, 0, 0)
circlecolor = (255, 255, 255)
circleradius = 20

rectY = 100
rectspeed = 5

pygame.init()
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
while True
    clock.tick(60)
    for event in pygame








    if pressed_keys[K_UP]:
        rectY = rectY - rectspeed
    if pressed_keys[K_DOWN]:
        rectY = rectY + rectspeed

    pygame.display.update()
# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
