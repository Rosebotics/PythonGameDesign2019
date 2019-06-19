# My first Pygame program.
# Authors: Many people and Jason <PUT-YOUR-NAME-HERE>

import pygame
import sys
import time

backgroundColor = (255, 255, 250)

white = (0, 100, 100)
circleLocation = (300, 200)
circleRadius = 20
circleX = 300
circleY = 200
circleSpeed = 1
pygame.init()

screen = pygame.display.set_mode((640, 480))  # My first Pygame program.
green = (0, 255, 0)
x = 300
y = 200

while True:
    #time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x = x + 1
    if pressed_keys[pygame.K_LEFT]:
        x = x - 1
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, green, (x,y), 30)

   # circleRadius = circleRadius+1

   # pygame.draw.circle(screen, white, (circleX,circleY), circleRadius)
    #pygame.draw.circle(screen, (255, 0, 0), circleLocation, circleRadius // 2)
    pygame.display.update()
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
