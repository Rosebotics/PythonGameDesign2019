# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and <Bryer#>

import pygame
import sys
screensize=(640, 480)
pygame.init()
screen = pygame.display.set_mode(screensize)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys, exit()
            BackgroundColor=(100, 0, 50)
    screen.fill((BackgroundColor))
    pygame.display.update()


