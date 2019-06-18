# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.

# I want To Break My Computer
# Authors: Derek, Professor Dave, and Becca
import time
import pygame
import sys

backgroundColor = (255, 255, 255)
realwhite = (0,0,0)
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




circleRadius1 = 4
circleRadius = 20
circleSpeed = 1

pygame.init()
screen = pygame.display.set_mode((640, 480))
Green = (0,255,0)
x = 300
y = 250
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [pygame.K_RIGHT]:
        x = x + 1
    if pressed_keys[pygame.K_LEFT]:
        x = x - 1
    if pressed_keys[pygame.K_DOWN]:
        y = y + 1
    if pressed_keys[pygame.K_UP]:
        y = y - 1
    screen.fill(backgroundColor)


    pygame.draw.circle(screen,Green,(x,y),30)



    pygame.display.update()



    pygame.display.update()
