# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
screenSize=(640,480)
backgroundcolor=(0,255,255)

rectY=100
rectSpeed=1

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            sys.exit()
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        rectY=rectY-rectSpeed
    if pressed_keys[K_DOWN]:
        rectY=rectY+rectSpeed
    screen.fill(backgroundcolor)


    print(rectY)

    pygame.draw.circle(screen,(255,89,0),(560,440),20)
    pygame.draw.rect(screen,(255,255,255),(600,rectY,20,75))
    pygame.display.update()