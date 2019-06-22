# My first Pygame program.
# Authors: Many people and Marika

import pygame
import sys
from pygame.locals import *

print()
print('GAME START')

player1 = 0
player2 = 0

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (150, 80, 255)
rectColor2 = (255, 100, 120)
rectColor1 = (100, 120, 255)
circleRadius = 20

rectY1 = 100
rectY2 = 100
rectX1 = 600
rectX2 = 20
circleX = 320
circleY = 240
circleXSpeed = 5
circleYSpeed = 2
rectSpeed = 5

pygame.init()
pygame.display.set_caption("pong")
pygame.key.set_repeat(1, 10)

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY1 = rectY1 - 5
        if pressed_keys[K_DOWN]:
            rectY1 = rectY1 + 5
        if pressed_keys[K_w]:
            rectY2 = rectY2 - 5
        if pressed_keys[K_s]:
            rectY2 = rectY2 + 5

        if rectY1 > 405:
            rectY1 = rectY1 -5
        if rectY1 < 0:
            rectY1 = rectY1 + 5
        if rectY2 > 405:
            rectY2 = rectY2 -5
        if rectY2 < 0:
            rectY2 = rectY2 + 5
    if player1 == 10:
        continue
    if player2 == 10:
        continue

    circleX = circleX + circleXSpeed
    if circleX > 620 or circleX < 20:
        circleXSpeed = circleXSpeed * -1

    circleY = circleY + circleYSpeed
    if circleY > 460 or circleY < 20:
        circleYSpeed = circleYSpeed * -1

    collided1 = pygame.Rect(rectX1, rectY1, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rectX2, rectY2, 20, 75).collidepoint(circleX - circleRadius, circleY)

    if collided1:
        circleXSpeed = circleXSpeed * -1
        player1 = player1 + 1
        print('player 1:', player1)

    if collided2:
        circleXSpeed = circleXSpeed * -1
        player2 = player2 + 1
        print('player 2:', player2)







    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, rectColor1, (rectX1, rectY1, 20, 75))
    pygame.draw.rect(screen, rectColor2, (rectX2, rectY2, 20, 75))

    pygame.display.update()

