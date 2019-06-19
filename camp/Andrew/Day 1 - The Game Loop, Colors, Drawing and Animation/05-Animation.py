
import pygame
import sys
import time
screen = pygame.display.set_mode((640, 480))
backcolor = (124, 132 , 200)
white = (255, 255, 255)
circleloc = (320, 240)
circlerad: int = 20
rectX = 600
rectY = 95
rectWidth = 20
rectLength = 75

rectSpeed = 1

pygame.draw.circle(screen, white, circleloc, circlerad)


pygame.init()
screen = pygame.display.set_mode((640, 480))
while True:
    for event in pygame.event.get():
          if event.type  == pygame.QUIT:
              sys.exit()

    screen.fill(backcolor)
    circlerad = circlerad + 50
    time.sleep(0.02)
    if circlerad > 450:
        circlerad = 20
    pygame.draw.circle(screen, white, circleloc, circlerad)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectLength))
    pygame.display.update()


