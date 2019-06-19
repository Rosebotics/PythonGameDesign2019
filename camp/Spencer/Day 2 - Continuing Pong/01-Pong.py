# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (255, 255, 255)


rectY = 100
rect2Y = 100
rectX = 600
rect2X = 40
rectSpeed = 8

circleX = 320
circleY = 230
circleXSpeed = 5
circleYSpeed = 3
circleRadius = 20

pygame.init()
pygame.display.set_caption("Pong")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
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
            rect2Y = rect2Y - rectSpeed
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed

    screen.fill(backgroundColor)
    circleX = circleX + circleXSpeed
    circleY = circleY + circleYSpeed
    if circleX > 620:
        circleXSpeed = -5
    if circleX < 20:
        circleXSpeed = 5
    circleY = circleY + circleYSpeed
    if circleY > 460:
        circleYSpeed = -3
    if circleY < 20:
        circleYSpeed = 3

    collided1 = pygame.Rect(rectX, rectY, 20, 80).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rect2X, rect2Y, 20, 80).collidepoint(circleX - circleRadius, circleY)
    if collided1 or collided2:
        circleXSpeed = circleXSpeed - 5



    pygame.draw.circle(screen, circleColor, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, (255, 255, 255), (rectX, rectY, 15, 75))
    pygame.draw.rect(screen, (255, 255, 255), (rect2X, rect2Y, -15, 75))
    pygame.display.update()


