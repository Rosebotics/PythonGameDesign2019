# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 255, 255)
circleColor = (255, 255, 255)
circleRadius = 20
circleX=320
circleY=240
circleXSpeed=5
circleYSpeed=2
rectX=600
rectx2=20
rectY = 100

rect2Y=100
rectSpeed = 5

pygame.init()
pygame.display.set_caption('Pong!')
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
            rect2Y=rect2Y-rectSpeed
        if pressed_keys[K_s]:
            rect2Y=rect2Y+rectSpeed
    # fill background before drawing
    screen.fill(backgroundColor)

    circleX=circleX+circleXSpeed
    if circleX > 620 or circleX < 20:
        circleXSpeed = -circleXSpeed

    circleY=circleY+circleYSpeed
    if circleY <20 or circleY>460:
        circleYSpeed=-circleYSpeed

    if rectY<0 or rectY >500:
        rectSpeed=-rectSpeed
    if rect2Y<0 or rect2Y>500:
        rectSpeed=-rectSpeed
    collided1 = pygame.Rect(rectX,rectY,20,75).collidepoint(circleX+circleRadius,circleY)
    collided2 = pygame.Rect(rectx2, rect2Y, 20, 75).collidepoint(circleX -circleRadius, circleY)
    if collided1 or collided2:
        circleXSpeed =circleXSpeed *-1
    pygame.draw.circle(screen, circleColor, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, (0, 255, 0), (rectX, rectY, 20, 75))
    pygame.draw.rect(screen,(255,0,255),(rectx2,rect2Y,20,75))

    pygame.display.update()
