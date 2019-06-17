# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# My first Pygame program.
# Authors: Many people and Marika

import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (160,100,255)
circleRadius =  20

pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((backgroundColor))

    pygame.draw.circle(screen, (circleColor), (320, 150), circleRadius)
    pygame.draw.rect(screen, (255,255,190), (600,100, 20, 75))
    pygame.display.update()
