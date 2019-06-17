import pygame
import sys
from pygame.locals import *

screenSize = (640,480)
backroundcolor = (0,0,0)
circleColor = (255,255,255)
circleRadius = (20)
rectY = 100
rectSpeed = 5
rect2Y = 100
rectSpeed2 = 5

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
            rectY = rectY - rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_w]:
            rect2Y = rect2Y - rectSpeed2
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed2





    screen.fill((backroundcolor))
    pygame.draw.circle(screen, (circleColor),(315,225), circleRadius)
    pygame.draw.rect(screen,(255,255,255),(600,rectY,20,75))
    pygame.draw.rect(screen,(255, 255, 255),(20,rect2Y,20,75))

    pygame.display.update()
