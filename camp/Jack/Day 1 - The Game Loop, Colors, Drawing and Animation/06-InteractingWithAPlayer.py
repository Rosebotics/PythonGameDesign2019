# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys
from  pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
CircleColor = (255, 255, 255)
CircleRadius = 20

rectY = 100
recty = 100
circleX = 100
circleSpeed = 5
rectSpeed = 5

pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        rectY = rectY - 3
    if pressed_keys[K_DOWN]:
        rectY = rectY + 3
    if pressed_keys[K_w]:
        recty = recty - 3
    if pressed_keys[K_s]:
        recty = recty + 3
    circleX = circleX + circleSpeed
    if circleX > 640:
        circleSpeed = -5
    if circleX < 0:
        circleSpeed = 5
    # fill background before drawing
    screen.fill((backgroundColor))

    pygame.draw.circle(screen, CircleColor, (circleX, 150), CircleRadius)
    pygame.draw.rect(screen, (255, 0, 0), (600, rectY, 20, 75))
    pygame.draw.rect(screen, (255, 0, 0), (40, recty, 20, 75))

    pygame.display.update()
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
