# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (132, 0, 122)
circleColor = (255, 255, 255)
circleRadius = 20

rectY = 100
rectSpeed = 5
rectY2 = 100
rectSpeed = 5
x = 250
y = 155
xSpeed = 1
ySpeed = 1



pygame.init()
pygame.display.set_caption("The Small Tennis")
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
            rectY = rectY - rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_w]:
            rectY2 = rectY2 - rectSpeed
        if pressed_keys[K_s]:
            rectY2 = rectY2 + rectSpeed
    x = x + xSpeed
    y = y + ySpeed





    # fill background before drawing
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    pad1 = (600, rectY, 20, 75)
    pad2 = (58, rectY2, 20, 75)
    if xSpeed > 0:
        edge = x + 20

    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed
    if pygame.Rect(50, rectY2, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed

    if y < 0:
        ySpeed = -ySpeed
    if x < 0:
        xSpeed = -xSpeed



    pygame.draw.rect(screen, (195, 70, 170), pad1)
    pygame.draw.rect(screen, (250, 60, 110), pad2)

    pygame.display.update()
