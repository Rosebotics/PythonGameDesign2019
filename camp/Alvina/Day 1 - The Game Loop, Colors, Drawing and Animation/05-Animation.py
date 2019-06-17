# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
#  Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and Alvina

import pygame
import sys
import pygame
import sys
import time
backgroundColor = (167, 79, 235)
white =(225, 225,225)
circlelocation=(320, 90)
circleRadius = (50)

rectX = 300
rectY = 140
rectWidth = 40
rectHeight = 130

rectSpeed = 1
circleSpeed = 1
pygame.init()

screen = pygame.display.set_mode((640, 480))
while True:
    time.sleep(0.0006)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(backgroundColor)

    circleRadius = circleRadius + 1
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()



