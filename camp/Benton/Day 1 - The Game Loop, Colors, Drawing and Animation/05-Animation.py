# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0,0,255)
circleColor = (255,255,255)
circleRadius = (20)
rectY = 100
rectangleSpeed = 5
pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rectY = rectY + rectangleSpeed
    if rectY > 405:
        rectangleSpeed = -5
    elif rectY < 0:
        rectangleSpeed = 5

    screen.fill(backgroundColor)
    pygame.draw.circle(screen, (circleColor), (300, 150), circleRadius)
    pygame.draw.rect(screen, (255,255,255), (600, rectY,20,75))
    pygame.display.update()
