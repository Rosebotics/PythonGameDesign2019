# My first Pygame program.
# Authors: Many people and Nidha Rajoli

import pygame
import sys
import time
backgroundColor = (100, 34, 188)
white = (255, 255, 0)
circlelocation = (300, 150)
circleRadius = 180

rectX = 96
rectY = 196
rectWidth = 176
rectHeight = 186

pygame.display.set_mode((640, 480))

pygame.init()
screen = pygame.display.set_mode((640, 480))
green = (0, 255, 0)
x = 300
y = 280

while True:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x = x + 1
    if pressed_keys[pygame.K_LEFT]:
        x = x - 1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_DOWN]:
        y = y + 1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:



        screen.fill(backgroundColor)
    pygame.draw.circle(screen, green, (x, y), 30)
    circleRadius = circleRadius + 1
    #pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()
