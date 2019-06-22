# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (100, 255, 200)
circleColor = (255, 255, 255)
circleRadius = 20

rectY = 100
rectSpeed = 10
circleSpeed = 5
pygame.init()
screen = pygame.display.set_mode((screenSize))
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
            rectY = rectY - rectSpeed
        if pressed_keys[K_s]:
            rectY = rectY + rectSpeed

    screen.fill((backgroundColor))

    pygame.draw.circle(screen, circleColor, (300, 150), circleRadius)
    pygame.draw.rect(screen, (0, 0, 0), (600, rectY, 20, 75))

    pygame.display.update()

