# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# My first Pygame program.
# Authors: Many people and mark

import pygame
import sys

backgroundColor = (255,255,255)
pink =(255,0,0)
circlelocation = (300,460)
circleRadius = 20
yellow = 255,255,0

rectX =0
rectY =400
rectwidth =20
rectheight = 75


circleSpeed = .1
pygame.init()
screen = pygame.display.set_mode((640, 480))
direction = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(backgroundColor)                               

        circleRadius = circleRadius + direction
        pygame.draw.circle(screen,pink,circlelocation,circleRadius)
        pygame.draw.circle(screen,yellow,circlelocation,circleRadius-5)
        pygame.draw.rect (screen,pink,(rectX,rectY, rectwidth, rectheight))
        pygame.display.update()
        if circleRadius > 500:
            direction = - direction
            pygame.draw.circle(screen,pink,circlelocation,circleRadius)
            pygame.draw.circle(screen,yellow,circlelocation,circleRadius-5)
            pygame.draw.rect (screen,pink,(rectX,rectY, rectwidth, rectheight))
            pygame.display.update()