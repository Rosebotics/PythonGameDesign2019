# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import random

import pygame
import sys
from pygame.locals import *

import pygame
import sys
from pygame.locals import*


class Ball:

    def __init__(self, screen, x, y, xSpeed, ySpeed, color, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color
        self.radius = radius

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
        if (self.x - self.radius) <= 0 or (self.x + self.radius) >= self.screen.get_width():
            self.xSpeed = self.xSpeed * -1
        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= self.screen.get_height():
            self.ySpeed = self.ySpeed * -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def collided(self):
        self.xSpeed = self.xSpeed * -1



screenSize = (640,480)
backroundcolor = (255,255,255)
# circlecolor = (0,0,0)
# circleradius = 20
# circlexspeed = 5
# circleyspeed = 5
# circlex = 320
# circley = 240
rectYone = 100
rectY = 100
rectspeed = 5
rectx = 610
rect2x = 10

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1,10)

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball= Ball(screen, 320, 240, 5, 5, (0, 0, 0), 20)

balls = [ball]



while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY - rectspeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectspeed
        if pressed_keys[K_w]:
            rectYone = rectYone - rectspeed
        if pressed_keys[K_s]:
            rectYone = rectYone + rectspeed


        if rectY > 405:
            rectY = 405
        if rectY < 0:
            rectY = 0
        if rectYone > 405:
            rectYone = 405
        if rectYone < 0:
            rectYone = 0





    #     ball.xSpeed = ball.xSpeed * -1

    screen.fill(backroundcolor)

    # pygame.draw.circle(screen, (circlecolor), (circlex, circley), circleradius)
    pygame.draw.rect(screen, (0,0,220), (rectx, rectY, 20, 100))
    pygame.draw.rect(screen, (180,30,0), (rect2x, rectYone, 20,100))
    toAdd = []
    for ball in balls:
        ball.move()
        ball.draw()

        collided1 = pygame.Rect(rectx, rectY, 20, 75).collidepoint(ball.x + ball.radius, ball.y)
        collided2 = pygame.Rect(rect2x, rectYone, 20, 75).collidepoint(ball.x - ball.radius, ball.y)

        if collided1 or collided2:
            ball.collided()

        if collided1 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x-5 , ball.y, -random.randint(2,6), random.randint(1,3), (0, 0, 0), 20))

        if collided2 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x+5, ball.y, random.randint(2,6), random.randint(1,3), (0, 0, 0), 20))

    for ball in toAdd:
        balls.append(ball)

    pygame.display.update()