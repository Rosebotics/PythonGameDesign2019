import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0,0,255)
circleColor = (255,255,255)
circleRadius = (20)
rectY = 100
rectangleSpeed = 5
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
            rectY = rectY - 10
        if pressed_keys[K_DOWN]:
            rectY = rectY + 10

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, (circleColor), (300, 150), circleRadius)
    pygame.draw.rect(screen, (255,255,255), (600, rectY,20,75))
    pygame.display.update()
