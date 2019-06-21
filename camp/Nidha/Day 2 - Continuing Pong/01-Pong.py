# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import random
balllist = []
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
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)),
                           self.radius)

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
        self.radius = self.radius + 1

        if self.x < 0 or self.x > self.screen.get_width():
            self.bouncex()
            balllist.append(Ball((random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), 10,random.randint(8, 648), 240,  self.screen, -self.xSpeed, -self.ySpeed))

        if self.y < 0 or self.y > self.screen.get_height():
            self.bouncey()

        if self.radius > 200:
            self.radius = 20


    def bouncex(self):
        self.xSpeed = self.xSpeed * -1
    def bouncey(self):
        self.ySpeed = self.ySpeed * -1

screenSize = (640, 480)
backgroundColor = (132, 0, 122)
circleColor = (255, 255, 255)
circleRadius = 20

rectY = 100
rectSpeed = 5
rectY2 = 100
rectSpeed = 5
x = 250
y = 155
xSpeed = 1
ySpeed = 1



pygame.init()
pygame.display.set_caption("The Small Tennis")
pygame.key.set_repeat(1,10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball((189, 0, 122), 20, 300, 200, screen, 1, 1)
ball2 = Ball((200, 0, 130), 30, 200, 180, screen, 2, 2)
ball3 = Ball((225, 0, 225), 50, 290, 128, screen, -1, -1)
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
            rectY2 = rectY2 - rectSpeed
        if pressed_keys[K_s]:
            rectY2 = rectY2 + rectSpeed
    x = x + xSpeed
    y = y + ySpeed






    # fill background before drawing
    screen.fill(backgroundColor)

    # pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()




    pad1 = (600, rectY, 20, 75)
    pad2 = (58, rectY2, 20, 75)
    if xSpeed > 0:
        edge = x + 20

    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed
        ySpeed = -ySpeed
    if pygame.Rect(50, rectY2, 20, 75).collidepoint(edge, y):
        xSpeed = -xSpeed

    if y < 0:

        ySpeed = -ySpeed
    if x < 0:
        xSpeed = -xSpeed



    pygame.draw.rect(screen, (195, 70, 170), pad1)
    pygame.draw.rect(screen, (250, 60, 110), pad2)

    pygame.display.update()









