# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import random

import pygame
import sys
from pygame.locals import *



class Ball:
    def __init__ (self, screen, x, y, xSpeed, ySpeed, color, radius):
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
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collided(self):
        self.xSpeed = self.xSpeed * -1.02



screenSize = (640, 480)
backgroundColor = (20, 40, 255)
circleColor = (1, 0, 30)
circleRadius = 20
circleX = 320
circleY = 240
circleXSpeed = 5
circleYSpeed = 2

rectX = 600
rect2X = 20

rectY = 100
rect2Y = 100
rectSpeed = 10

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1, 10)

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball(screen, 320, 240, 5, 2, (25, 255, 255), 20)
balls = [ball]





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

    screen.fill(backgroundColor)


    toAdd = []
    for ball in balls:
        ball.move()
        ball.draw()




        collided1 = pygame.Rect(rectX, rectY, 20, 75). collidepoint(ball.x + ball.radius, ball.y)
        collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(ball.x - ball.radius, ball.y)

        if collided1 or collided2:
           ball.collided()


        if collided1 and len (balls) < 100:
            toAdd.append(Ball(screen,ball.x, ball.y, -random.randint(2,6), random.randint(1,3), (255, 255, 255), 20))
        if collided2 and len (balls) < 100:
            toAdd.append(Ball(screen, ball.x, ball.y, random.randint(2, 6), random.randint(1, 3), (255, 255, 255), 20))

    for ball in toAdd:
        balls.append(ball)



    #pygame.draw.circle(screen, circleColor, (int(circleX), int(circleY)), circleRadius)
    #rect1
    pygame.draw.rect(screen, (134, 200, 240), (rectX, rectY, 20, 75))
    #rect2
    pygame.draw.rect(screen, (20, 155, 255),  (rect2X, rect2Y, 20, 75))


    ball.move()
    ball.draw()

    pygame.display.update()
