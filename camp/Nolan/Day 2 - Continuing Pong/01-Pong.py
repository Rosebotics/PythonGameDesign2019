import pygame
import sys
from pygame.locals import *

screenSize = (640,480)
backroundcolor = (0,0,0)
circleColor = (255,255,255)
circleRadius = (20)
circleSpeed = (5)
rectY = 100
rectSpeed = 5
rect2Y = 100
rectSpeed2 = 5
circleX = 320
circleY = 240
circleYSpeed = 2
circleXSpeed = 5
rectX = 600
rect2X = 20
pygame.init()
pygame.display.set_caption("Pong")
pygame.key.set_repeat(1,10)
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

    circleX = circleX + circleXSpeed
    if circleX > 628:
        circleXSpeed = -5
    elif circleX < 15:
        circleXSpeed = 5
    circleY = circleY + circleYSpeed
    if circleY > 461:
        circleYSpeed = -2
    elif circleY < 20:
        circleYSpeed = 2

    collided1 = pygame.Rect(rectX, rectY,20,75).collidepoint(circleX + circleRadius,circleY)
    collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(circleX - circleRadius, circleY)
    if collided1 or collided2 :
        circleXSpeed = circleXSpeed * -1.02

    screen.fill((backroundcolor))
    pygame.draw.circle(screen, (circleColor),(int(circleX),int(circleY)), circleRadius)
    pygame.draw.rect(screen,(255,255,255),(rectX,rectY,20,75))
    pygame.draw.rect(screen,(255, 255, 255),(rect2X,rect2Y,20,75))

    pygame.display.update()

