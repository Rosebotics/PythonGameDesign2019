# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
xspeed = 2
yspeed = 2
screenSize = (640, 480)
backgroundColor = (255, 0, 0)
circleColor = (255, 255, 255)
circleRadius = 20
X = 300
Y = 150

rectY = 100
rectY2 = 100
rectSpeed: int = 5

pygame.init()
pygame.display.set_caption("PoNg")
pygame.key.set_repeat(1, 10)
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

    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    paddle1 = (600, rectY, 20 ,75)
    paddle2 = (40, rectY2, 20, 75)
    if xspeed > 0:
        edge = X + 20
    else:
        edge = X - 20


    if pygame.Rect(600, rectY, 20 ,75).collidepoint(edge,Y):
        xspeed = -xspeed * 2
        yspeed = -yspeed * 2
    if pygame.Rect(40, rectY2, 20, 75).collidepoint(edge, Y):
        xspeed = -xspeed
        yspeed = -yspeed

    if Y < 0:
        yspeed = -yspeed
    if X < 0:
        xspeed = -xspeed
    if Y > 480:
        yspeed = -yspeed
    if X > 640:
        xspeed = -xspeed



    pygame.draw.rect(screen, (255, 255, 0), paddle1)
    pygame.draw.rect(screen,  (0, 0, 255),  paddle2)
    X = X + xspeed
    Y = Y + yspeed

    pygame.display.update()
