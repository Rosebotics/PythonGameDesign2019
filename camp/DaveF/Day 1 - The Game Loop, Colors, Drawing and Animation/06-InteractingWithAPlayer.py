# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# TODO: Copy all of your   04-Drawing.py   program and put it below this comment. Yay!
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 50, 100)
circleColor = (255, 255, 255)
circleRadius = 20
rectColor = (255, 255, 50)

rectY= 100
rect2Y =100
rectSpeed = 5

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
            rectY = rectY - 3
        if pressed_keys[K_DOWN]:
            rectY = rectY + 3
        if pressed_keys[K_w]:
            rect2Y = rect2Y - 3
        if pressed_keys[K_s]:
            rect2Y = rect2Y + 3
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (300, 150), circleRadius)
    pygame.draw.rect(screen, rectColor, (600, rectY, 20, 100))
    pygame.draw.rect(screen, rectColor, (20, rect2Y, 20, 100))
    pygame.display.update()