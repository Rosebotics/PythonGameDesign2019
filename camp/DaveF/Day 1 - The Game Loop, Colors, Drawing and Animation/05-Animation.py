# TODO: Copy all of your   04-Drawing.py   program and put it below this comment. Yay!
import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 50, 100)
circleColor = (255, 255, 255)
circleRadius = 20
rectColor = (255, 255, 50)

rectY= 100
rectSpeed = 5

pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (300, 150), circleRadius)
    rectY = rectY + rectSpeed
    if rectY > 380 or rectY < 0:
        rectSpeed = -rectSpeed

    print(rectSpeed)

    pygame.draw.rect(screen, rectColor, (600, rectY, 20, 100))
    pygame.display.update()

