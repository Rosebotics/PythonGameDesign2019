


# My first Pygame program.
# Authors: Many people and Nidha Rajoli


import pygame
import sys
import time
screen = pygame.display.set_mode((460, 780))
backgroundColor = (100, 188, 218)
backgroundColor = (100, 34, 188)
white = (255, 255, 0)
circlelocation=(300, 150)
circleRadius=(180)

rectX = 16
rectY = 26
rectWidth = 36
rectHeight = 46




pygame.display.set_mode((640, 480))

pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit()
         screen.fill(backgroundColor)
    circleRadius = circleRadius + 2
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))

    pygame.display.update()
