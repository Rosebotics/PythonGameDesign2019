# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import random
balllist = []
class Ball:
    def __init__(self, color, radius, x, y, screen, xspeed, yspeed):
        self.color =color
        self.radius=radius
        self.x=x
        self.y=y
        self.screen=screen
        self.xspeed=xspeed
        self.yspeed=yspeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        self.radius = self.radius + 1


        if self.x <0 or self.x > 640:
            self.bouncex()
            balllist.append(Ball(self.color, 10, 320, 240, self.screen, -self.xspeed, -self.yspeed))

        if self.y <0 or self.y > 480:
           self.bouncey()
           balllist.append(Ball(self.color, 10, 320, 240, self.screen, -self.xspeed, -self.yspeed))

    def bouncex(self):
        self.xspeed = self.xspeed * -1

    def bouncey(self):
        self.yspeed = self.yspeed *-1
        
        if self.radius >100:
            self.radius = 0

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
circleColor = (255, 255, 255)
circleRadius = 20
x = 200
y = 0
rectY = 100
rectSpeed = 5
rectY2 = 100
rectSpeed2 = 5
xspeed=4
yspeed=4
pygame.init()
pygame.display.set_caption("any polite title")
pygame.key.set_repeat(1, 1)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball((0, 0, 255), 20, 50, 200, screen, 9, 9)
ball2 = Ball((255, 0, 0), 20,50, 240, screen, 9, 9)
ball3 = Ball((255, 255, 0), 20,50, 125, screen, 9, 9)
ball4 = Ball((0, 255, 255), 20,25, 100, screen, 9, 9)
ball5 = Ball((255, 0, 255), 20,25, 75, screen, 9, 9)
ball6 = Ball((255, 255, 255), 20,25, 50, screen, 9, 9)
ball7 = Ball((200, 255, 255), 20,640, 25, screen, 9, 9)
ball8 = Ball((255, 150, 255), 20,640, 10, screen, 9, 9)
ball9 = Ball((255, 255, 68), 20,640, 0, screen, 9, 9)


balllist.append(ball)
balllist.append(ball2)
balllist.append(ball3)
balllist.append(ball4)
balllist.append(ball5)
balllist.append(ball6)
balllist.append(ball7)
balllist.append(ball8)
balllist.append(ball9)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            rectY = rectY - rectSpeed
        if pressed_keys[K_s]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_UP]:
            rectY2 = rectY2-rectSpeed2
        if pressed_keys[K_DOWN]:
            rectY2 = rectY2+rectSpeed2

    x = x + xspeed
    y = y + yspeed

    # fill background before drawing
    screen.fill(backgroundColor)

    #pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()

    pad1 = (20, rectY, 20, 75)
    pad2 = (600, rectY2, 20, 75)

    if xspeed > 0:
        edge = x + 20
    else:
        edge = x - 20
    #if pygame.Rect(20, rectY, 20, 75).collidepoint(edge, y):
    #    xspeed = -xspeed *2
    #    yspeed = -yspeed *1


    #if pygame.Rect(600, rectY2, 20, 75).collidepoint(edge, y):
    #       xspeed = -xspeed * 1
    #       yspeed = -yspeed * 1
    if y < 0:
            yspeed = -yspeed
    if y > 480:
        yspeed = -yspeed
    if x < 0:
        xspeed = -xspeed
    if x > 640:
        xspeed = -xspeed

    pygame.draw.rect(screen, (255, 255, 255), pad1)
    pygame.draw.rect(screen, (255, 255, 255), pad2)
    pygame.display.update()
