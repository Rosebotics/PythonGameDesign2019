# My first Pygame program.
# Authors: Many people and Jason <PUT-YOUR-NAME-HERE>

import pygame
import sys
import time

backgroundColor = (255, 255, 250)

white = (0, 100, 100)
circleLocation = (300, 200)
circleRadius = 20
circleX = 300
circleY = 200
circleSpeed = 1
pygame.init()

screen = pygame.display.set_mode((640, 480))  # My first Pygame program.

while True:
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    circleRadius = circleRadius+1

    pygame.draw.circle(screen, white, (circleX, circleY), circleRadius)
    pygame.draw.circle(screen, (255, 0, 0), circleLocation, circleRadius // 2)
    pygame.display.update()
