# TODO: Copy all of your   05-Animation.py   program and put it below this comment.


import pygame
import sys
from pygame.locals import*
screenSize = (640,480)
backroundcolor = (0,200,220)
circlecolor = (0,0,0)
circleradius = 20
rectYone = 100
rectY = 100
rectspeed = 5

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
            rectY = rectY - rectspeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectspeed
        if pressed_keys[K_w]:
            rectYone = rectYone - rectspeed
        if pressed_keys[K_s]:
            rectYone = rectYone +rectspeed

    screen.fill(backroundcolor)




    pygame.draw.circle(screen, (circlecolor), (300, 150), circleradius)
    pygame.draw.rect(screen, (230,0,240), (600, rectY, 20, 75))
    pygame.draw.rect(screen, (230,0,240), (40, rectYone, 20,75))


    pygame.display.update()
