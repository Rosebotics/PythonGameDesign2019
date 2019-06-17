# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# Sloth Jaws
# Authors: Derek, Professor Dave, and Becca
import time
import pygame
import sys

backgroundColor = (255, 255, 255)

orange=(40,90,200)
white= (225,100,100)
circleLocation = (300,50)
circleLocation2= (200,50)
circleLocation3= (100,50)
circleLocation4= (400,50)
circleLocation5= (500,50)
circleLocation6= (600,50)
circleLocation0= (0,50)
circleLocation1= (300,450)
circleLocation21= (200,450)
circleLocation31= (100,450)
circleLocation41= (400,450)
circleLocation51= (500,450)
circleLocation61= (600,450)
circleLocation01= (0,450)





circleRadius = 20
circleSpeed = 1

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (backgroundColor)
    time.sleep(0.95)
    circleRadius = circleRadius + 1
    pygame.draw.circle(screen,white,circleLocation,circleRadius)
    pygame.draw.circle(screen,white,circleLocation2, circleRadius)
    pygame.draw.circle(screen,white,circleLocation3,circleRadius)
    pygame.draw.circle(screen,white,circleLocation4,circleRadius)
    pygame.draw.circle(screen,white,circleLocation5,circleRadius)
    pygame.draw.circle(screen,white,circleLocation6, circleRadius)
    pygame.draw.circle(screen,white,circleLocation0, circleRadius)
    pygame.draw.circle(screen,white,circleLocation1,circleRadius)
    pygame.draw.circle(screen,white,circleLocation21, circleRadius)
    pygame.draw.circle(screen,white,circleLocation31,circleRadius)
    pygame.draw.circle(screen,white,circleLocation41,circleRadius)
    pygame.draw.circle(screen,white,circleLocation51, circleRadius)
    pygame.draw.circle(screen,white,circleLocation61,circleRadius)
    pygame.draw.circle(screen,white,circleLocation01,circleRadius)
    pygame.display.update()
    time.sleep(0.95)
    circleRadius=circleRadius+1
    pygame.draw.circle(screen,orange,circleLocation,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation2,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation3,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation4,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation5,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation6,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation0, circleRadius)
    pygame.draw.circle(screen,orange,circleLocation1,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation21,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation31,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation41,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation51,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation01,circleRadius)
    pygame.draw.circle(screen,orange,circleLocation61,circleRadius)

    pygame.display.update()
