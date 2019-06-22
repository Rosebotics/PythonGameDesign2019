# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import random
ballist = []
class Ball:
    def __init__(self, color, radius, x, y, screen, xspeed, yspeed):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.screen = screen
        self.xspeed = xspeed
        self.yspeed = yspeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)
    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        self.radius = self.radius + 1
        if self.x < 0 or self.x >self.screen.get_width():
            self.bouncex()
            ballist.append(Ball(self.color, 10, 320, 240, self.screen, -self.xspeed, -self.yspeed))
            self.radius = 20

        if self.y < 0 or self.y > self.screen.get_height():
            self.bouncey()

        if self.radius > 1000:
            self.radius = 20
    def bouncex(self):
        self.xspeed = self.xspeed * -1
    def bouncey(self):
        self.yspeed = self.yspeed * -1

screenSize = (640, 480)
backgroundColor = (20, 220, 235)
circleColor = (255, 255, 255)
circleRadius = 20


rectY = 100
rectSpeed = 5

x = 300
y = 150

xSpeed = 2
ySpeed = 2

rect2 = 100


pygame.init()
pygame.display.set_caption('YAY')
pygame.key.set_repeat(1,10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball((5,4, 87), 20, 3, 300, screen, 1, 1)
ball2 = Ball((0, 30, 255), 20, 190, 65, screen, 1, 1)
ball3 = Ball((0, 25, 56), 20, 57, 80, screen, 1,1)
ball4 = Ball((0, 90, 200), 20, 400, 133, screen, 1, 1)
ballist.append(ball)
ballist.append(ball2)
ballist.append(ball3)
ballist.append(ball4)
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
                rect2 = rect2 - rectSpeed
        if pressed_keys[K_e]:
                rect2 = rect2 + rectSpeed
    x = x + xSpeed
    y = y + ySpeed

    # fill background before drawing
    screen.fill(backgroundColor)

    # pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    for b in ballist:
        b.draw()
        b.move()

    pad1 = (600, rectY, 20, 75)
    pad2 = (40, rect2, 20, 75)
    if xSpeed > 0:
        edge = x + 20
    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge,y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed
    if pygame.Rect(40, rect2, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed


    if y < 0:
        ySpeed = -ySpeed
    if x < 0:
        xSpeed = -xSpeed
    if y > 480:
        ySpeed = -ySpeed
    if x > 640:
        xSpeed = -xSpeed

    pygame.draw.rect(screen, (195, 70, 170), pad1)
    pygame.draw.rect(screen, (255, 45, 95), pad2)

    pygame.display.update()
