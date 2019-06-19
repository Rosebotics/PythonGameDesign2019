#
# My first Pygame program.
# Authors: Many people and mark

import pygame
import sys
import time

backgroundColor = (0,255,255)
pink =(40,0,0)
blue=(0,0,40)
circlelocation = (300,263)
circleRadius = 20
yellow = 0,255,0

rectX =0
rectY =400
rectwidth =20
rectheight = 75

rectX=30
rectY=15
rectwidth=400
rectheight=60
circleSpeed = .1

pygame.init()
screen = pygame.display.set_mode((640, 480))

direction = 1
green=(0,255,0)
x=300
y=200

while True:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x=x+1
    if pressed_keys[pygame.K_LEFT]:
        x=x-1
    if pressed_keys[pygame.K_UP]:
        y=y-1
    if pressed_keys[pygame.K_DOWN]:
        y=y+1
    screen.fill(backgroundColor)
    pygame.draw.circle(screen,green,(x,y),30)

    #circleRadius = circleRadius + direction
    pygame.draw.circle(screen,pink,circlelocation,circleRadius)
    pygame.draw.circle(screen,yellow,circlelocation,circleRadius-5)

    pygame.display.update()
    if circleRadius > 500:
        direction = - direction
        pygame.draw.circle(screen,pink,circlelocation,circleRadius)
        pygame.draw.circle(screen,yellow,circlelocation,circleRadius-5)
        pygame.draw.rect (screen,blue,(rectX,rectY, rectwidth, rectheight))
        pygame.draw.circle(screen,blue,circlelocation,circleRadius)

        pygame.display.update()

