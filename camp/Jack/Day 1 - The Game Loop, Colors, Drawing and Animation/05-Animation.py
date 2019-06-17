# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
CircleColor = (255, 255, 255)
CircleRadius = 20

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

    # fill background before drawing
    screen.fill((backgroundColor))
    rectY = rectY + rectSpeed
    if rectY > 480:
        rectSpeed = -5
    elif rectY < 0:
        rectSpeed = 5

    pygame.draw.circle(screen, CircleColor, (300, 150), CircleRadius)
    pygame.draw.rect(screen, (255, 0, 0), (600, rectY, 20, 75))

    pygame.display.update()
