# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  03-Colors.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)scree
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

import pygame
import sys

screensize=(640, 488)
backgroundcolor= (255, 0, 0)
circlecolor= (255, 255, 255)
circleradius= 20
pygame.init()
screen = pygame.display.set_mode(screensize)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #remember to fill backround BEFORE drawing

    screen.fill((0, 255, 0))
    pygame.draw.circle(screen, circlecolor, (300, 350), circleradius)
    pygame.draw.rect(screen, (255, 255, 0), (600, 100, 20, 75))

    pygame.display.update()
