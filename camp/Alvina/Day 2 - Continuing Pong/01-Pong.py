# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (20, 220, 235)
circleColor = (255, 255, 255)
circleRadius = 20


rectY = 100
rectSpeed = 5

x = 300
y = 150

xSpeed = 2
ySpeed = 2

rect2 = 100


pygame.init()
pygame.display.set_caption('YAY')
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
                rect2 = rect2 - rectSpeed
        if pressed_keys[K_e]:
                rect2 = rect2 + rectSpeed
    x = x + xSpeed
    y = y + ySpeed

    # fill background before drawing
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    pad1 = (600, rectY, 20, 75)
    pad2 = (40, rect2, 20, 75)
    if xSpeed > 0:
        edge = x + 20
    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge,y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed
    if pygame.Rect(40, rect2, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed


    if y < 0:
        ySpeed = -ySpeed
    if x < 0:
        xSpeed = -xSpeed
    if y > 480:
        ySpeed = -ySpeed
    if x > 640:
        xSpeed = -xSpeed

    pygame.draw.rect(screen, (195, 70, 170), pad1)
    pygame.draw.rect(screen, (255, 45, 95), pad2)

    pygame.display.update()
