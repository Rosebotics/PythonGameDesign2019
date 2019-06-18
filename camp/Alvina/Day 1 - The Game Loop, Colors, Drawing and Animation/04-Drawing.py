#  Control-V (to PASTE the copied code into this file.
# My first Pygame program.
# Authors: Many people and Alvina

import pygame
import sys
import pygame
import sys
backgroundColor = (167, 79, 235)
white =(225, 225,225)
circlelocation=(320, 90)
circleRadius = (50)

rectX = 300
rectY = 140
rectWidth = 40
rectHeight = 150

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

screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(backgroundColor)
    pygame.draw.circle(screen, white, circlelocation, circleRadius)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectHeight))
    pygame.draw.rect(screen, white, (rectXa, rectYa, rectWidtha, rectHeighta))
    pygame.draw.rect(screen, white, (rectXb, rectYb, rectWidthb, rectHeightb))
    pygame.draw.circle(screen, black, circlelocationa, circleRadiusa)
    pygame.draw.circle(screen, black, circlelocationb, circleRadiusb)
    pygame.draw.rect(screen, white, (rectXc, rectYc, rectWidthc, rectHeightc))

    pygame.display.update()



