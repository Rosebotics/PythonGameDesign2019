# TODO: Copy all of your   02-TheGameLoop.py   program and put it below this comment.
# TODO    One way to do so is:
# TODO      1. Inside  02-TheGameLoop.py,  do:
# TODO           -- Control-A (to SELECT the entire contents of the file, then
# TODO           -- Control-C (to COPY that entire selection)
# TODO      2. Inside this file:
# TODO           -- Click below this comment, then
# TODO           -- Control-V (to PASTE the copied code into this file.

# My first Pygame program.
# Authors: Martin W.

import pygame
import sys
import time

backgroundColor = (255, 255, 0)
pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time.sleep(0.5)
    screen.fill(backgroundColor)
    pygame.display.update()

    time.sleep(0.5)
    screen.fill((0, 0, 255))
    pygame.display.update()






# TODO: With your instructor's help (live coding):
#   - Put your name as an author.
#   - Make the game loop be able to stop more gracefully.
