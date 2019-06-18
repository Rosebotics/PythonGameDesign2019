
# My first Pygame program.
# Authors: Many people and Derek
import time
import pygame
import sys

backgroundColor = (50, 255, 50)

orange=(40,90,200)
white= (225,0,225)
circleLocation = (300,150)
circleLocation2= (200,150)
circleLocation3= (100,150)
circleLocation4= (400,150)
circleLocation5= (500,150)
circleRadius = 20

rectX = 500
rectY = 150
rectWidth = 20
rectHeight = 75
pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (backgroundColor)
    time.sleep(1)
    pygame.draw.circle(screen,white,circleLocation,circleRadius)
    pygame.draw.circle(screen,white,circleLocation2, circleRadius)
    pygame.draw.circle(screen,white,circleLocation3,circleRadius)
    pygame.draw.circle(screen,white,circleLocation4,circleRadius)
    pygame.draw.circle(screen,white,circleLocation5,circleRadius)
    pygame.display.update()
    time.sleep(1)
    pygame.draw.circle(screen,orange,circleLocation,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation2,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation3,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation4,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation5,circleRadius)

    pygame.display.update()


