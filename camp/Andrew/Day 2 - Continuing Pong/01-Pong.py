
import pygame
import sys
from pygame.locals import *
import random

balllist = []

class Ball:
    def __init__(self, color,radius,x,y, screen,xspeed,yspeed):
        self.color= color
        self.radius= radius
        self.x= x
        self.y= y
        self.screen = screen
        self.xspeed= xspeed
        self.yspeed= yspeed
        self.screen= screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed




        if self.x < 0:
            self.bouncex()
            balllist.append(Ball(self.color, 10, 340, 260, self.screen, -self.xspeed, -self.yspeed))
        if self.x > 640:
            self.bouncex()
        if self.y < 0:
            self.bouncey()
        if self.y > 480:
            self.bouncey()



    def bouncex(self):
        self.xspeed = self.xspeed * -1

    def bouncey(self):
        self.yspeed = self.yspeed * -1
xspeed = 2
yspeed = 2
screenSize = (640, 480)
backgroundColor = (255, 255, 0)
circleColor = (255, 255, 255)
circleRadius = 20
X = 300
Y = 150

rectY = 100
rectY2 = 100
rectSpeed: int = 5

pygame.init()
pygame.display.set_caption("PoNg")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball= Ball((255,255,255),25, 300, 200, screen, 5, 12)
ball2= Ball((255,255,255),25, 234, 255, screen, 5, 3)
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
            rectY2 = rectY2 - rectSpeed
        if pressed_keys[K_s]:
            rectY2 = rectY2 + rectSpeed

    screen.fill(backgroundColor)

    #pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    for b in balllist:
       b.draw()
       b.move()


    paddle1 = (600, rectY, 20 ,75)
    paddle2 = (40, rectY2, 20, 75)
    if xspeed > 0:
        edge = X + 20
    else:
        edge = X - 20


    if pygame.Rect(600,rectY,20,75).collidepoint(edge,Y):
        xspeed = -xspeed + 3
        yspeed = -yspeed + 3
    if pygame.Rect(40, rectY2, 20, 75).collidepoint(edge, Y):
        xspeed = -xspeed + 3
        yspeed = -yspeed + 3

    if Y < 0:
        yspeed = -yspeed
    if X < 0:
        xspeed = -xspeed
    if Y > 480:
        yspeed = -yspeed
    if X > 640:
        xspeed = -xspeed



    pygame.draw.rect(screen, (255, 0, 0), paddle1)
    pygame.draw.rect(screen,  (0, 0, 255),  paddle2)
    X = X + xspeed
    Y = Y + yspeed

    pygame.display.update()
