
import pygame
import sys
import time

backgroundColor = (255, 255, 255)

white = (0, 100, 100)
circleLocation = (300, 150)
circleRadius = 20

pygame.init()

screen = pygame.display.set_mode((640, 480))# My first Pygame program.

while True:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circleLocation, circleRadius)
    pygame.draw.circle(screen,(255, 0, 0),circleLocation,circleRadius//2)
    pygame.display.update()