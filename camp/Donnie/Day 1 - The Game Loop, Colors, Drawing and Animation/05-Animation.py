

import pygame
import sys
import time

white = (255, 0, 200)
circlexy = (320, 240)
circleRA =480
width =310

white2 = (255, 255, 255)
circlexy2 = (430, 425)
circleRA2 =50
width2 =5

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



color = (0, 200, 0)
pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(color)
    pygame.draw.circle(screen, white, circlexy, circleRA, width)
    if circleRA >399:

        circleRA = circleRA -1
    pygame.draw.circle(screen, white2, circlexy2, circleRA2, width2)
    pygame.display.update()



















