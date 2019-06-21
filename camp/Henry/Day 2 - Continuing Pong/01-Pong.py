# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 200)
circleColor = (255, 255, 255)
circleRadius = 20
circleX = 320
circleXSpeed = 5
circleY = 240
circleYSpeed = 2
rectX = 600
rectX2 = 20
rectY = 100
rectY2 = 100
rectSpeed = 5

pygame.init()
pygame.display.set_caption("pong")
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
        if pressed_keys [K_w]:
            rectY2 = rectY2 - rectSpeed
        if pressed_keys [K_s]:
            rectY2 = rectY2 + rectSpeed

    circleY = circleY + circleYSpeed

    if circleY > 460 or circleY < 20:
        circleYSpeed = circleYSpeed * -1

    circleX = circleX + circleXSpeed

    if circleX > 620 or circleX < 20:
        circleXSpeed = circleXSpeed * -1

    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(rectX2, rectY2, 20, 75).collidepoint(circleX - circleRadius, circleY)
    if collided1 or collided2:
        circleXSpeed = circleXSpeed *-1.02
    # fill background before drawing
    screen.fill(backgroundColor)


    pygame.draw.circle(screen, circleColor, (int(circleX), int(circleY)), circleRadius)
    pygame.draw.rect(screen, (255, 255, 255), (rectX, rectY, 20, 75))
    pygame.draw.rect(screen, (255, 255, 255), (rectX2, rectY2, 20, 75))

    pygame.display.update()
