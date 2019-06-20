import pygame
import sys

screenSize = 640, 480
backgroundColor = (255, 0, 0)
circleColor = (255, 255, 255)
circleRadius = 20

# TODO: Make the circle bounce

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
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            rectY = rectY - rectSpeed
        if pressed_keys[pygame.K_DOWN]:
            rectY = rectY + rectSpeed

    # fill background before drawing
    screen.fill(backgroundColor)

    pygame.draw.circle(screen, circleColor, (300, 150), circleRadius)
    pygame.draw.rect(screen, (255, 255, 0), (600, rectY, 20, 75))

    pygame.display.update()
