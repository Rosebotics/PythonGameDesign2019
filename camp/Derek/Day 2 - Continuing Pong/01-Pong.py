# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (20, 225, 20)
circleColor = (220, 0, 0)
circleRadius = 20
X = 300
Y = 150
XSpeed = 1
YSpeed = 1

rectY2=100
rectY = 100
rectSpeed = 5

pygame.init()
pygame.display.set_caption("Colorful Ping Pong")
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
        if rectY<0:
            rectY = 0
        if rectY2<0:
            rectY2 = 0
        if rectY>410:
            rectY = 410
        if rectY2>410:
            rectY2 = 410

    X = X + XSpeed
    Y = Y + YSpeed

    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    pad1 = (600, rectY, 20, 75)
    pad2 = (50, rectY2, 20, 75)
    if XSpeed> 0:
        edge = X + 20
    else:
        edge = X - 20
    if pygame.Rect(600,rectY,20,75).collidepoint(edge,Y):
       XSpeed = -XSpeed*2
       #YSpeed = -YSpeed
    if pygame.Rect(50, rectY2, 20, 75).collidepoint(edge,Y):
       XSpeed = -XSpeed*2
       #YSpeed = -YSpeed

    if Y < 0:
        YSpeed = -YSpeed
    if X < 0:
        XSpeed = -XSpeed
    if Y >480:
        YSpeed = -YSpeed
    if X >640:
        XSpeed = -XSpeed


    pygame.draw.rect(screen, (255, 255, 0), pad1)
    pygame.draw.rect(screen,(0,255,255),pad2)

    pygame.display.update()
