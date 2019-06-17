# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.


# My first Pygame program.
# Authors: Many people and Saujin

import pygame
import sys
screenSize = (640,480)
backroundcolor = (0,200,220)
circlecolor = (0,0,0)
circleradius = 20

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
    screen.fill(backroundcolor)
    rectY = rectY + rectspeed
    if rectY > 405:
        rectspeed = -5
    elif rectY < 0:
        rectspeed = 5
    print(rectY)

    pygame.draw.circle(screen, (circlecolor), (300, 150), circleradius)
    pygame.draw.rect(screen, (230,0,240), (600, rectY, 20, 75))


    pygame.display.update()