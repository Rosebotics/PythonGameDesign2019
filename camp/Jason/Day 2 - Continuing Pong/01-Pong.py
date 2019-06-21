# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import  random
balllist = []

class Ball:
    def __init__(self, color, radius, x, y, screen, xspeed, yspeed):
        self.color = color
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.screen = screen
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x = self.x +self.xspeed
        self.y = self.y + self.yspeed
        #self.radius = self.radius + 1

        if self.x < 0 or self.x > self.screen.get_width():
            self.bouncex()
            balllist.append(Ball((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), random.randint(5, 30), 320, 240, self.screen, -self.xspeed, -self.yspeed))

        if self.y < 0 or self.y > self.screen.get_height():
            self.bouncey()

        if self.radius > 200:
            self.radius = 20

    def bouncex(self):
        self.xspeed = self.xspeed * -1

    def bouncey(self):
        self.yspeed = self.yspeed * -1


screenSize = (640, 480)
backgroundColor = (255, 0, 0)
circleRadius = 20
circleColor = (0,255, 0)

rectY = 100
rectY2 = 100
rectSpeed = 5
x = 300
y = 150
xspeed=-5
yspeed=1

pygame.init()
pygame.display.set_caption("sticks")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()



ball1 = Ball((0, 255, 0), 20, 300, 200, screen, 4, 4)
ball2 = Ball((0, 255, 0), 20, 0, 200, screen, 4, 4)
balllist.append(ball1)
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
    x=x+xspeed
    y=y+yspeed
    # fill background before drawingif pressed_keys[K_UP]:

    screen.fill(backgroundColor)

   # pygame.draw.circle(screen, circleColor, (x, y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()
    pad1 = (600, rectY, 20, 75)
    pad2 = (40, rectY2, 20, 75)
    if xspeed > 0:
        edge = x + 20

    else:
        edge = x - 20
    if pygame.Rect(600, rectY, 20, 75).collidepoint(edge, y):
        xspeed = -xspeed * 1
       # yspeed = -yspeed * 1
    if pygame.Rect(40, rectY2,20, 75).collidepoint(edge, y):
        xspeed = -xspeed * 1
        #yspeed = -yspeed * 1

    if y < 0:
        yspeed = - yspeed
    if x < 0:
        xspeed = -xspeed
    if y > 480:
        yspeed = -yspeed
    if x > 640:
        xspeed = -xspeed



    pygame.draw.rect(screen, (255, 255, 0), pad1)
    pygame.draw.rect(screen, (100, 155, 0), pad2)
    pygame.display.update()
