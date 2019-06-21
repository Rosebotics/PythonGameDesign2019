#

# My first Pygame program.
# Authors: Many people and Arya

import pygame
import sys
import time

color = (134, 225, 135)

white = (255, 99, 79)
circlelocation = (320, 240)
circleradius = 150

whitea = (167, 79, 120)
circlelocation = (320, 240)
circleradius = 150
circlexa = 400
circleya = 200

whiteb = (0, 0, 0)
circlelocation = (320, 240)
circleradius = 150
circlexb = 300
circleyb = 220

rectX = 330
rectY = 250
rectWidth = 50
rectHeight =175

rectspeed = 1
circlesspeed = 1
circlex = 300
circley = 200

pygame.init()
screen = pygame.display.set_mode((640, 480))

orange = (255, 175, 45)
x = 300
y = 200

while True:
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x = x + 1
    if pressed_keys[pygame.K_LEFT]:
        x = x - 1
    if pressed_keys[pygame.K_DOWN]:
        y = y + 1
    if pressed_keys[pygame.K_UP]:
        y = y - 1
    screen.fill(color)
    pygame.draw.circle(screen, orange, (x, y), 30)


    circleradius = circleradius - 2
    circlex = circlex + 2
    circley = circley - 2
    circlexa = circlexa + 1
    circleya = circleya - 2
    circlexb = circlexb + 1
    circleyb = circleyb - 2
    rectHeight = rectHeight - 2
    rectWidth = rectWidth - 2

    pygame.draw.circle(screen, white, (circlex, circley), circleradius)
    pygame.draw.circle(screen, whitea, (circlexa, circleya), circleradius)
    pygame.draw.circle(screen, whiteb, (circlexb, circleyb), circleradius)
    pygame.draw.rect(screen,white, (rectX, rectY, rectWidth, rectHeight))
    pygame.display.update()



# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
