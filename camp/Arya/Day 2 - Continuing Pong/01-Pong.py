# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import random

balllist =[]

class Ball:
    def __init__(self, color, radius, x, y, screen, xSpeed, ySpeed):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.screen = screen
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
        self.radius = self.radius + 1


        if self.x < 0 or self.x > self.screen.get_width():
            self.bouncex()
            balllist.append(Ball(self.color, 10, 320, 240, self.screen, -self.xSpeed, -self.ySpeed))
            self.radius = 20
        if self.y < 0 or self.y > self.screen.get_height():
            self.bouncey()
            self.radius = 20

        if self.radius > 150:
            self.radius = 1

    def bouncex(self):
        self.xSpeed = self.xSpeed * -1

    def bouncey(self):
        self.ySpeed = self.ySpeed * -1




screenSize = (640, 480)
backgroundColor = (255, 99, 79)
circleColor = (255, 255, 255)
circleRadius = 20

rectY = 100
rectSpeed = 5

rectYa = 100
rectSpeeda = 5

x = 300
y = 150

xspeed = 2
yspeed = 2

pygame.init()
pygame.display.set_caption("COOKIE!")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball((167, 79, 255), 20, 320, 240, screen, 0.5, 0.5)
ball2 = Ball((125, 10, 155), 20, 320, 240, screen, -0.5, 0)
ball3 = Ball((134, 255, 135), 20, 320, 240, screen, -0.5, 0.5)
balllist.append(ball)
balllist.append(ball2)
balllist.append(ball3)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY - rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_w]:
            rectYa = rectYa - rectSpeeda
        if pressed_keys[K_s]:
            rectYa = rectYa + rectSpeeda
    x = x + xspeed
    y = y + yspeed
    # fill background before drawing
    screen.fill(backgroundColor)


    # pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()


    cookie1 = (600, rectY, 20, 75)
    cookie2 = (40, rectYa, 20, 75)
    if xspeed > 0:
        edge = x + 20
    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge, y):
        xspeed = -xspeed
        yspeed = -yspeed
    if pygame.Rect(40, rectYa, 20, 75).collidepoint(edge, y):
        xspeed = -xspeed
        yspeed = -yspeed
    if y < 0:
        yspeed = -yspeed
    if x < 0:
        xspeed = -xspeed
    if y > 480:
        yspeed = -yspeed
    if x > 640:
        xspeed = -xspeed



    pygame.draw.rect(screen, (134, 255, 135), cookie1)
    pygame.draw.rect(screen, (255, 175, 45), cookie2)

    pygame.display.update()
