


# My first Pygame program.
# Authors: Many people and Nidha Rajoli


import pygame
import sys
import time
screen = pygame.display.set_mode((460, 780))
backgroundColor = (100, 188, 218)
backgroundColor = (100, 34, 188)
white = (255, 255, 0)
circlelocation=(300, 150)
circleRadius=(180)

rectX = 16
rectY = 26
rectWidth = 36
rectHeight = 46




pygame.display.set_mode((640, 480))# TODO: Copy all of your   03-Colors.py   program and put it below this comment.
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
# Authors: Many people and Nidha Rajoli


import pygame
import sys
backgroundColor = (100, 188, 218)
backgroundColor = (100, 34, 188)
white = (255, 255, 0)
circlelocation=(300, 150)
circleRadius=(180)
pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit()
    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (12, 32, 53, 65))
    pygame.display.update()



while True:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit()
         screen.fill(backgroundColor)
    circleRadius = circleRadius + 2
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))

    pygame.display.update()
