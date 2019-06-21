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


rectXa = 330
rectYa = 160
rectWidtha = 110
rectHeighta = 25

rectXb = 200
rectYb = 160
rectWidthb = 110
rectHeightb = 25

rectXc = 160
rectYc = 90
rectWidthc = 25
rectHeightc = 110

black = (0, 0, 0)
circlelocationa=(300, 85)
circleRadiusa = (7)

circlelocationb=(350,85 )
circleRadiusb =(7)

pygame.init()


green = (0, 111, 0)
x = 350
y = 75


screen = pygame.display.set_mode((640, 480))
while True:
    time.sleep(0.06)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x = x + 1
    if pressed_keys [pygame.K_LEFT]:
        x = x - 1
    if pressed_keys [pygame.K_DOWN]:
        y = y + 1
    if pressed_keys [pygame.K_UP]:
        y = y - 1

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, green, (x, y), 30)
    circleRadius = circleRadius - 1
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.draw.rect(screen, white, (rectXa, rectYa, rectWidtha, rectHeighta))
    pygame.draw.rect(screen, white, (rectXb, rectYb, rectWidthb, rectHeightb))
    pygame.draw.circle(screen, black, circlelocationa, circleRadiusa)
    pygame.draw.circle(screen, black, circlelocationb, circleRadiusb)
    pygame.draw.rect(screen, white, (rectXc, rectYc, rectWidthc, rectHeightc))

    pygame.display.update()



