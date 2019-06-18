# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

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
            pressed

    screen.fill(backgroundcolor)

    rectY=rectY+rectSpeed
    if rectY>480:
        rectSpeed=-1

    elif rectY<0:
        rectSpeed=1

    print(rectY)

    pygame.draw.circle(screen,(255,89,0),(560,440),20)
    pygame.draw.rect(screen,(255,255,255),(600,rectY,20,75))
    pygame.display.update()