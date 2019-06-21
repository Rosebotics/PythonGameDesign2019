# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# My first Pygame program.
# Authors: Many people and Spencer

import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (255, 255, 255)
circlePos = (320, 230)
rectY = 100
rectSpeed = 4




pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(backgroundColor)
    rectY = rectY + rectSpeed
    if rectY > 405:
        rectSpeed = -4
    if rectY < 0:
        rectSpeed = 4

    print(rectY)
    pygame.draw.circle(screen, circleColor, circlePos, 20)
    pygame.draw.rect(screen, (circleColor), (600, rectY, 20, 75))
    pygame.draw.rect(screen, (circleColor), (40, rectY, 20, 75))
    pygame.display.update()
