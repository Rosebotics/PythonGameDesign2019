# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and <Bryer#>

import pygame
import sys

rectY=100
rectspeed=6

screensize=(640, 480)
BackgroundColor=(125, 0, 50)
CircleColor=(255, 255, 255)
CircleRadius=20


pygame.init()
screen = pygame.display.set_mode(screensize)
clock= pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (BackgroundColor)

    rectY= rectY+rectspeed
    print(rectY)
    if rectY>405:rectspeed= -6
    if rectY<0:rectspeed=6

    pygame.draw.circle(screen, CircleColor, (300, 150), CircleRadius)
    pygame.draw.rect(screen, (60, 180, 0), (600, rectY, 20, 75))
    pygame.display.update()
