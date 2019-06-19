# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)

backgroundColor = (0, 0, 0)

circleColor = (150, 0, 255)
circleRadius = 20
Xspeed = 2
Yspeed = 2

rectY = 100
rect2Y = 100
rectSpeed = 5

X = 300
Y = 150

pygame.init()
pygame.display.set_caption("Pong")
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
            rect2Y = rect2Y - rectSpeed
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed
        if rectY<0:
            rectY = 0
        if rect2Y<0:
            rect2Y = 0
        if rectY>400:
            rectY = 400
        if rect2Y>400:
            rect2Y = 400

    X = X + Xspeed
    Y = Y + Yspeed

    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    Paddle1 = (600, rectY, 20, 80)
    Paddle2 = (20, rect2Y, 20, 80)
    if Xspeed > 0:
        edge = X + 20

    else:
        edge = X - 20
    if pygame.Rect(600, rectY, 20, 80).collidepoint(edge, Y):
        Xspeed = -Xspeed
        #Yspeed = -Yspeed
    if pygame.Rect(20, rect2Y, 20, 80).collidepoint(edge, Y):
        Xspeed = -Xspeed
        #Yspeed = -Yspeed

    if Y < 20:
        Yspeed = -Yspeed
    if X < 20:
        Xspeed = -Xspeed
    if Y > 460:
        Yspeed = -Yspeed
    if X > 620:
        Xspeed = -Xspeed

    pygame.draw.rect(screen, (0, 0, 255), Paddle1)
    pygame.draw.rect(screen, (255, 0, 0), Paddle2)

    pygame.display.update()
