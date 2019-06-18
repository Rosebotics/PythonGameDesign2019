# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

class Ball:
    def __init__(self, screen, x, y, xSpeed, ySpeed, color, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color
        self.radius = radius









screenSize = (640, 480)
backgroundColor = (0, 0, 255)
dotColor = (255, 255, 255)
circleRadius = 20
circleX = 320
circleY = 240

rectY = 380
rect2Y = 20
ballXSpeed = 5
ballYSpeed = 2
rectSpeed = 5

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1,10)

# rect 1 600 rect 2 40

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY -rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_w]:
            rect2Y = rect2Y - rectSpeed
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed

    # fill background before drawing

    screen.fill(backgroundColor)

    circleX = circleX + ballXSpeed
    if circleX > 640 or circleX < 0:
        sys.exit()

    circleY = circleY + ballYSpeed
    if circleY > 460 or circleY < 20:
        ballYSpeed = ballYSpeed * -1

    collided1 = pygame.Rect(600, rectY, 20, 75).collidepoint(circleX + circleRadius, circleY)
    collided2 = pygame.Rect(20, rect2Y, 20, 75).collidepoint(circleX - circleRadius, circleY)

    if collided1:
        ballXSpeed = -5
    if collided2:
        ballXSpeed = 5

    pygame.draw.circle(screen, (255, 255, 255), (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, (255, 255, 255), (600, rectY, 20, 75))
    # rect 1
    pygame.draw.rect(screen, (255, 255, 255), (20, rect2Y, 20, 75))
    # rect 2
    pygame.display.update()
