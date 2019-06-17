# My first Pygame program.
# Authors: Many people and <Bryer#>

import pygame
import sys
from pygame.locals import *

rectY=100
rect_speed=6

screensize=(640, 480)
BackgroundColor=(125, 0, 50)
CircleColor=(255, 255, 255)
CircleRadius=20
rect2Y=100

pygame.init()
screen = pygame.display.set_mode(screensize)
clock= pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (BackgroundColor)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [K_UP]:
        rectY = rectY - rect_speed
    if pressed_keys [K_DOWN]:
        rectY = rectY + rect_speed

    pygame.draw.circle(screen, CircleColor, (300, 150), CircleRadius)
    pygame.draw.rect(screen, (60, 180, 0), (600, rectY, 20, 75))

    pygame.draw.rect(screen, (60, 180, 0), (20, rect2Y, 20, 75))
    pygame.display.update()
