# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (255, 0, 0)
circleColor = (255, 255, 255)
circleRadius = 20
circleX = 320
circleY = 240
circleXSpeed = 5
circleYSpeed = 2

rectX = 600
rect2X = 20

rectY = 100
rect2Y = 100
rectSpeed = 5

pygame.init()
pygame.display.set_caption("Pong!")
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

    # fill background before drawing
    screen.fill(backgroundColor)

    circleX = circleX + circleXSpeed
    if circleX > 640 or circleX < 0:
        circleXSpeed = circleXSpeed * -1

    circleY = circleY + circleYSpeed
    if circleY > 480 or circleY < 0:
        circleYSpeed = circleYSpeed * -1

    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(circleX - circleRadius, circleY)

    if collided1 or collided2:
        circleXSpeed = circleXSpeed * -1.02
    pygame.draw.circle(screen, circleColor, (int(circleX), int(circleY)), circleRadius)
    #rect1
    pygame.draw.rect(screen, (255, 255, 0), (rectX, rectY, 20, 75))
    #rect2
    pygame.draw.rect(screen, (255, 0, 255), (rect2X, rect2Y, 20, 75))

    pygame.display.update()
