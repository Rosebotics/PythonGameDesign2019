# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

import pygame
import sys
from pygame.locals import*
screenSize = (640,480)
backroundcolor = (255,255,255)
circlecolor = (0,0,0)
circleradius = 20
circlexspeed = 5
circleyspeed = 5
circlex = 320
circley = 240
rectYone = 100
rectY = 100
rectspeed = 5
rectx = 600
rect2x = 40

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1,10)

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
            rectYone = rectYone + rectspeed


        if rectY > 405:
            rectY = 405
        if rectY < 0:
            rectY = 0
        if rectYone > 405:
            rectYone = 405
        if rectYone < 0:
            rectYone = 0



    circlex = circlex + circlexspeed
    circley = circley + circleyspeed
    if circlex > 620:
        circlexspeed = -5
    if circlex < 20:
        circlexspeed = 5
    if circley > 460:
        circleyspeed = -5
    if circley < 20:
        circleyspeed = 5


    collided1 = pygame.Rect(rectx,rectY, 20,75).collidepoint(circlex + circleradius, circley)
    collided2 = pygame.Rect(rect2x, rectYone, 20,75).collidepoint(circlex - circleradius, circley)

    if collided1 or collided2:
        circlexspeed = circlexspeed * -1
    screen.fill(backroundcolor)

    pygame.draw.circle(screen, (circlecolor), (circlex, circley), circleradius)
    pygame.draw.rect(screen, (0,0,220), (rectx, rectY, 20, 75))
    pygame.draw.rect(screen, (180,30,0), (rect2x, rectYone, 20,75))


    pygame.display.update()