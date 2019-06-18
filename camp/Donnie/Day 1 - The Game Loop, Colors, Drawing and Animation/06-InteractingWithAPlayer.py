




circspeed =1

color = (0, 200, 0)

import pygame
import sys
import time

white = (255, 0, 200)
circlexy = (320, 240)
circleRA =700
width =319

white2 = (255, 255, 255)
circlexy2 = (320, 240)
circleRA2 =85
width2 =5

pygame.init()
screen = pygame.display.set_mode((640, 480))

red = (220, 0, 0)
x = 320
y = 240
RA = 10
wide = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_d]:
        x = x+1
    if pressed_keys[pygame.K_a]:
        x = x-1
    if pressed_keys[pygame.K_s]:
        y = y+1
    if pressed_keys[pygame.K_w]:
        y = y-1
    if pressed_keys[pygame.K_SLASH]:
        RA = RA-1
    if pressed_keys[pygame.K_SPACE]:
        RA = RA +1
    screen.fill(color)
    pygame.draw.circle(screen, red, (x, y), RA, wide)
    pygame.draw.circle(screen, white, circlexy, circleRA, width)
    if circleRA >399:

        circleRA = circleRA -1
    pygame.draw.circle(screen, white2, circlexy2, circleRA2, width2)
    pygame.display.update()

