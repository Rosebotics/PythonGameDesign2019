
import pygame
import sys
import time

backcolor = (124, 132 , 200)
white = (255, 255, 255)
circleloc = (320, 240)
circlerad = 320
width = 319
rectX = 600
rectY = 95
rectWidth = 20
rectLength = 75


pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
          if event.type  == pygame.QUIT:
              sys.exit()

    screen.fill(backcolor)
    pygame.draw.circle(screen, white, circleloc, circlerad, width)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectLength))
    pygame.draw.circle2(screen, white, circleloc, circlerad, width)
    pygame.display.update()

