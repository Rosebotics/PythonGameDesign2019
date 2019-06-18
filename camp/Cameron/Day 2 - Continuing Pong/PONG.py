# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *


class Ball:

    def __init__(self, screen, x, y, xSpeed, ySpeed, color, radius):
        self.x = x
        self.y = y
        self.screen = screen







circleX = 300
circleY = 150
screenSize = (640, 480)
backgroundColor = (0, 255, 0)
circleColor = (0, 0, 0)
circleRadius = 20

rectX2= 20
rectY2 = 100
rectSpeed = 10
circleXSpeed = 5
circleYSpeed = 2

rectX = 600
rectY = 200

pygame.init()
pygame.display.set_caption("Cameron's really really awesome videogame that is named Tim")
pygame.key.set_repeat(1, 10)

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ctY = rectSpeed
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        rectY = rectY - rectSpeed
    if pressed_keys[K_DOWN]:
        rectY = rectY + rectSpeed
    if pressed_keys[K_w]:
        rectY2 = rectY2 - rectSpeed
    if pressed_keys[K_s]:
        rectY2 = rectY2 + rectSpeed
    # fill background before drawing
    screen.fill(backgroundColor)

    circleX = circleX + circleXSpeed
    if circleX > 620 or circleX < 20:
        circleXSpeed = circleXSpeed * -1

    circleY = circleY + circleYSpeed
    if circleY > 420 or circleY < 20:
        circleYSpeed = circleYSpeed * -1

    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rectX2, rectY2, 20, 75).collidepoint(circleX - circleRadius, circleY)

    if collided1 or collided2:
        circleXSpeed = circleXSpeed * -1



    pygame.draw.circle(screen, circleColor, (circleX, circleY), circleRadius)
    #rect1
    pygame.draw.rect(screen, (255, 255, 0), (rectX, rectY, 20, 75))
    #rect2
    pygame.draw.rect(screen, (255, 0, 255), (rectX2, rectY2, 20, 75))

    pygame.display.update()
