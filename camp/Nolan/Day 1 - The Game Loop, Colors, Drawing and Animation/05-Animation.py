import pygame
import sys

screenSize = (640,480)
backroundcolor = (0,0,0)
circleColor = (255,255,255)
circleRadius = (20)
rectY = 100
rectSpeed = 5

pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((backroundcolor))
    rectY = rectY + rectSpeed
    print(rectY)
    if rectY > 405:
        rectSpeed = -5
    elif rectY < 0:
        rectSpeed = 5
    pygame.draw.circle(screen, (circleColor),(315,225), circleRadius)
    pygame.draw.rect(screen,(255,255,255),(600,rectY,20,75))


    pygame.display.update()

