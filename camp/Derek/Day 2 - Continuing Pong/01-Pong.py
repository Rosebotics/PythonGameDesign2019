# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *
import random
balllist =[]
class Ball:
    def __init__(self,color,radius,X,Y,screen,XSpeed,YSpeed):
        self.color = color
        self.radius = radius
        self.X = X
        self.Y = Y
        self.screen = screen
        self.XSpeed = XSpeed
        self.YSpeed = YSpeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color,(int(self.X),int(self.Y)),self.radius)
    def move(self):
        self.X= self.X + self.XSpeed
        self.Y= self.Y + self.YSpeed
        self.radius = self.radius +0

        if self.X <0 or self.X > self.screen.get_width():
            self.bouncex()
            balllist.append(Ball((random.randint(0,255),random.randint(0,255),random.randint(0,255)), 20, random.randint(0,640),random.randint(0,480),self.screen,-self.XSpeed, -self.YSpeed))

        if self.Y <0 or self.Y > self.screen.get_height():
            self.bouncey()




    def bouncex(self):
        self.XSpeed = self.XSpeed * -1

    def bouncey(self):
        self.YSpeed = self.YSpeed * -1

screenSize = (640, 480)
backgroundColor = (255, 255, 255)
circleColor = (220, 0, 0)
circleRadius = 20
X = 300
Y = 150
XSpeed = 10
YSpeed = 10

rectY2=100
rectY = 100
rectSpeed = 5

pygame.init()
pygame.display.set_caption("Colormeggadan")
pygame.key.set_repeat(1,10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()


ball= Ball((0, 255, 0), 20, 300, 200, screen, 4,4)
ball2 = Ball((255,0,0),20,400,100,screen,-4,-4)
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
        if rectY<0:
            rectY = 0
        if rectY2<0:
            rectY2 = 0
        if rectY>410:
            rectY = 410
        if rectY2>410:
            rectY2 = 410

    X = X + XSpeed
    Y = Y + YSpeed

    screen.fill(backgroundColor)

    #pygame.draw.circle(screen, circleColor, (X, Y), circleRadius)
    for b in balllist:
        b.draw()
        b.move()




    #pad1 = (600, rectY, 20, 75)
    #pad2 = (50, rectY2, 20, 75)
    if XSpeed> 0:
        edge = X + 20
    else:
        edge = X - 20
    if pygame.Rect(600,rectY,20,75).collidepoint(edge,Y):
       XSpeed = -XSpeed*1
       YSpeed = -YSpeed
    if pygame.Rect(50, rectY2, 20, 75).collidepoint(edge,Y):
       XSpeed = -XSpeed*1
       YSpeed = -YSpeed

    if Y < 0:
        YSpeed = -YSpeed
    if X < 0:
        XSpeed = -XSpeed
    if Y >480:
        YSpeed = -YSpeed
    if X >640:
        XSpeed = -XSpeed



    #pygame.draw.rect(screen, (255, 255, 0), pad1)
    #pygame.draw.rect(screen,(225,0,0),pad2)

    pygame.display.update()
