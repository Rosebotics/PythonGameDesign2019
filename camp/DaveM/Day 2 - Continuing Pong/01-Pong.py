# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (255, 0, 0)
circleColor = (255, 255, 255)
circleRadius = 20

rectY = 100
rect2Y = 400
rectSpeed = 5
x = 300
y = 150
xspeed = 1
yspeed = 1

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

    x = x + xspeed
    y = y + yspeed
    # fill background before drawing
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    pad1 = (600, rectY, 20, 75)
    pad2 = (40, rect2Y, 20, 75)
    if xspeed > 0:
        edge = x + 20
    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge, y):
        xspeed = -xspeed * 2
        yspeed = -yspeed * 2
    if pygame.Rect(40, rect2Y, 20, 75).collidepoint(edge, y):
        xspeed = -xspeed * 2
        yspeed = -yspeed * 2

    if y < 0:
        yspeed = -yspeed
    if x < 0:
        xspeed = -xspeed
    if y > 480:
        yspeed = -yspeed
    if x > 640:
        xspeed = -xspeed


    pygame.draw.rect(screen, (255, 255, 0), pad1)
    pygame.draw.rect(screen, (0, 255, 0), pad2)


    pygame.display.update()
