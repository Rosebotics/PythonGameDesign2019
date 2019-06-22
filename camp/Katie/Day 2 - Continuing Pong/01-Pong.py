# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# hi katie
# i see you in your sleeeep
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (100, 255, 200)
circleColor = (255, 255, 255)
circleRadius = 20
circleX = 320
circleY = 240
circleXSpeed = 5
circleYSpeed = 1

rectX = 600
rect2X = 20

rectY = 100
rect2Y = 100
rectSpeed = 5

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1,10)

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
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
        if pressed_keys[K_b]:
            pygame.draw.rect(screen, (backgroundColor), (600, rectY, 1000, 1000))

    circleX = circleX + circleXSpeed
    if (circleX) > 620:
        circleXSpeed = -5
    elif (circleX) < 20:
        circleXSpeed = 5
        print(circleX)


    circleY = circleY + circleYSpeed
    if circleY > 460:
        circleYSpeed = -1
    elif circleY < 20:
        circleYSpeed = 1
        print(circleY)

    # fill background before drawing
    screen.fill(backgroundColor)

    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(circleX - circleRadius, circleY)

    if collided1 or collided2:
        circleXSpeed = circleXSpeed * -1

    pygame.draw.circle(screen, circleColor, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, (0, 0, 0), (rectX, rectY, 20, 75))
    pygame.draw.rect(screen, (0, 0, 0), (rect2X, rect2Y, 20, 75))

    pygame.display.update()

    clock.tick(60)

