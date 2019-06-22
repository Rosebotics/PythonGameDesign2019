# My first Pygame program.
# Authors: Many people and Marika
import random

import pygame
import sys
from pygame.locals import *

class Ball:

    def __init__(self, screen, x, y, xSpeed ,ySpeed, color, radius):
        self.x = x
        self.y = y
        self.screen = screen
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color
        self.radius = radius

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed


        if (self.x - self.radius) < 0 or (self.x + self.radius) >= self.screen.get_width():
            self.xSpeed = self.xSpeed * -1
        if (self.y - self.radius) < 0 or (self.y + self.radius) >= self.screen.get_height():
             self.ySpeed = self.ySpeed * -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x),int(self.y)),self.radius)

    def collided(self):
        self.xSpeed = self.xSpeed * -1.02

print()
print('GAME START')



screenSize = (640, 480)
backgroundColor = (0, 0, 0)
rectColor2 = (255, 100, 120)
rectColor1 = (100, 120, 255)

rectY1 = 100
rectY2 = 100
rectX1 = 600
rectX2 = 20
rectSpeed = 5

pygame.init()
pygame.display.set_caption("pong")
pygame.key.set_repeat(1, 10)

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = Ball(screen, 320, 240, 5, 2, (150,80, 255), 20)
balls = [ball]

while True:
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY1 = rectY1 - 5
        if pressed_keys[K_DOWN]:
            rectY1 = rectY1 + 5
        if pressed_keys[K_w]:
            rectY2 = rectY2 - 5
        if pressed_keys[K_s]:
            rectY2 = rectY2 + 5

        # if rectY1 > 405:
        #     rectY1 = rectY1 -5
        # if rectY1 < 0:
        #     rectY1 = rectY1 + 5
        # if rectY2 > 405:
        #     rectY2 = rectY2 -5
        # if rectY2 < 0:
        #     rectY2 = rectY2 + 5

    screen.fill(backgroundColor)


    toAdd = []
    for ball in balls:
        ball.move()
        ball.draw()

        collided1 = pygame.Rect(rectX1, rectY1, 20, 75).collidepoint(ball.x + ball.radius, ball.y)
        collided2 = pygame.Rect(rectX2, rectY2, 20, 75).collidepoint(ball.x - ball.radius, ball.y)

        if collided1:
            ball.collided()
        if collided2:
            ball.collided()

        if collided1 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x-5, ball.y, -random.randint(2, 6), random.randint(1, 3), (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)), 20))
        if collided2 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x+5, ball.y, random.randint(2, 6), random.randint(1, 3), (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)), 20))



    for ball in toAdd:
        balls.append(ball)

    pygame.draw.rect(screen, rectColor1, (rectX1, rectY1, 20, 75))
    pygame.draw.rect(screen, rectColor2, (rectX2, rectY2, 20, 75))

    pygame.display.update()
