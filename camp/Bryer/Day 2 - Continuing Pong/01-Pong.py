# My first Pygame program.
# Authors: Many people and <Bryer#>

import pygame
import sys
from pygame.locals import *

CircleY=200
CircleX=300
circlexspeed =3
circleyspeed=4
rectY=100
rect_speed=6
rectX=20
rect2X=600

screensize=(640, 480)
BackgroundColor=(125, 0, 50)
CircleColor=(255, 255, 255)
CircleRadius=20
rect2Y=100

pygame.init()
pygame.display.set_caption("Pong!")
screen = pygame.display.set_mode(screensize)
clock= pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (BackgroundColor)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [K_w]:
        rectY = rectY - rect_speed
    if pressed_keys [K_s]:
        rectY = rectY + rect_speed

    if pressed_keys[K_DOWN]:
        rect2Y = rect2Y + rect_speed
    if pressed_keys[K_UP]:
        rect2Y = rect2Y - rect_speed

    CircleX = CircleX + circlexspeed
    print(CircleX)
    if CircleX > 628:
        circlexspeed = -6
    if CircleX < 12:
        circlexspeed = 6

    CircleY = CircleY - circleyspeed
    if CircleY < 20 or CircleY > 461:
        circleyspeed = -1 * circleyspeed

    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(CircleX - CircleRadius, CircleY)
    collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(CircleX + CircleRadius, CircleY)
    if collided1 or collided2 :
        circlexspeed = circlexspeed * -1

  #  pygame.draw.rect(screen, (255, 255, 0)())

    pygame.draw.circle(screen, CircleColor, (CircleX, CircleY), CircleRadius)
    pygame.draw.rect(screen, (60, 180, 0), (rectX, rectY, 20, 75))

    pygame.draw.rect(screen, (60, 180, 0), (rect2X, rect2Y, 20, 75))
    pygame.display.update()

