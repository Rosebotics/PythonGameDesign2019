



# TODO: Copy all of your   05-Animation.py   program and put it below this comment.


import pygame
import sys
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
green =  (0, 255, 0)
x=300
y=200
while True:
    for event in pygame.event.get():
          if event.type  == pygame.QUIT:
              sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        x =x +1
    if pressed_keys[pygame.K_LEFT]:
            x = x -1
    screen.fill(backcolor)
    pygame.draw.circle(screen, green, (x, y), 30)
    #circlerad = circlerad + 50
    if circlerad > 450:
        circlerad = 20
    pygame.draw.circle(screen, white, circleloc, circlerad)
    pygame.draw.rect(screen, white, (rectX, rectY, rectWidth, rectLength))
    pygame.display.update()
