import pygame
import sys
from pygame.locals import *
import random

balllist = []

class Ball:
    def __init__(self, color, radius, X, Y, screen, Xspeed, Yspeed):
        self.color = color
        self.radius = radius
        self.X = X
        self.Y = Y
        self.screen = screen
        self.Xspeed = Xspeed
        self.Yspeed = Yspeed
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.X), int(self.Y)), self.radius)

    def move(self):
        self.X = self.X + self.Xspeed
        self.Y = self.Y + self.Yspeed


        if self.X < 20 or self.X > self.screen.get_width()-20:
            self.bounceX()
            balllist.append(Ball((random.randint(0,255),random.randint(0,255),random.randint(0,255)), 20, random.randint(20,620), 240, self.screen, -self.Xspeed, -self.Yspeed))

            #self.radius = self.radius + 10

        if self.Y < 20 or self.Y > self.screen.get_width()-180:
            self.bounceY()

            #self.radius = self.radius + 10

        #if self.radius > 100:
            #self.radius = 20

    def bounceX(self):
        self.Xspeed = self.Xspeed * -1

    def bounceY(self):
        self.Yspeed = self.Yspeed * -1



screenSize = (640, 480)

backgroundColor = (0, 0, 0)

circleColor = (150, 0, 255)
circleRadius = 20
Xspeed = 1
Yspeed = 1

rectY = 100
rect2Y = 100
rectSpeed = 8

X = 300
Y = 150

pygame.init()
pygame.display.set_caption("Pong")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball((random.randint(0,255),random.randint(0,255),random.randint(0,255)), 20, 320, 220, screen, 6, 6)
ball2 = Ball((random.randint(0,255),random.randint(0,255),random.randint(0,255)), 20, 320, 260, screen, -6, -6)
balllist.append(ball)
balllist.append(ball2)

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
            rect2Y = rect2Y - rectSpeed
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed
        if rectY<0:
            rectY = 0
        if rect2Y<0:
            rect2Y = 0
        if rectY>400:
            rectY = 400
        if rect2Y>400:
            rect2Y = 400

    X = X + Xspeed
    Y = Y + Yspeed

    screen.fill(backgroundColor)

    #pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()

    Paddle1 = (600, rectY, 20, 80)
    Paddle2 = (20, rect2Y, 20, 80)
    if Xspeed > 0:
        edge = X + 20

    else:
        edge = X - 20
    if pygame.Rect(600, rectY, 20, 80).collidepoint(edge, Y):
        Xspeed = -Xspeed
        #Yspeed = -Yspeed
    if pygame.Rect(20, rect2Y, 20, 80).collidepoint(edge, Y):
        Xspeed = -Xspeed
        #Yspeed = -Yspeed

    if Y < 20:
        Yspeed = -Yspeed
    if X < 20:
        Xspeed = -Xspeed
    if Y > 460:
        Yspeed = -Yspeed
    if X > 620:
        Xspeed = -Xspeed

    pygame.draw.rect(screen, (0, 0, 255), Paddle1)
    pygame.draw.rect(screen, (255, 0, 0), Paddle2)

    pygame.display.update()
