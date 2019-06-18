# TODO: Copy all of your   03-Colors.py   program and put it below this comment. Boom!
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 100, 150)
circleColor = (255, 255, 255)
circleCenter = (300, 150)
circleRadius = 25
rectColor = (255, 255, 50)

pygame.init()
screen = pygame.display.set_mode(screenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, circleCenter, circleRadius)
    pygame.draw.rect(screen, rectColor, (600, 100, 20, 100))
    pygame.display.update()