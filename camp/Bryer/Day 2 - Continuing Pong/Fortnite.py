# My first Pygame program.
# Authors: Many people and <Bryer#>
import random

import pygame
import sys
from pygame.locals import *

class Ball:

    def __init__(self, screen, x, y, xspeed, yspeed, color, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.color = color
        self.radius = radius

    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed

        if (self.x - self.radius) <= 0 or (self.x + self.radius) >= self.screen.get_width():
            self.xspeed = self.xspeed * -1

        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= self.screen.get_height():
            self.yspeed = self.yspeed * -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collided(self):
        self.xspeed = self.xspeed * -1














rectY=100
rect_speed=6
rectX=20
rect2X=600

screensize=(640, 480)
BackgroundColor=(125, 0, 50)

rect2Y=100

pygame.init()
pygame.display.set_caption("Pong!")
screen = pygame.display.set_mode(screensize)
clock= pygame.time.Clock()

ball = Ball(screen, 320, 240, 3, 4, (255, 255, 255), 20)
balls = [ball]
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill (BackgroundColor)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [K_w]:
        rectY = rectY - rect_speed
    if pressed_keys [K_s]:
        rectY = rectY + rect_speed

    if pressed_keys[K_DOWN]:
        rect2Y = rect2Y + rect_speed
    if pressed_keys[K_UP]:
        rect2Y = rect2Y - rect_speed

    toAdd = []
    for ball in balls:
        ball.move()
        ball.draw()

        collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(ball.x - ball.radius, ball.y)
        collided2 = pygame.Rect(rect2X, rect2Y, 20, 75).collidepoint(ball.x + ball.radius, ball.y)

        if collided1 or collided2:
            ball.collided()

        if collided1 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x-5, ball.y, -random.randint(2, 6), random.randint(1, 3), (255, 255, 255), 20))
            ball.collided()
        if collided2 and len(balls) < 100:
            toAdd.append(Ball(screen, ball.x+5, ball.y, random.randint(2, 6), random.randint(1, 3), (255, 255, 255), 20))



    for ball in toAdd:
        balls.append(ball)



    pygame.draw.rect(screen, (60, 180, 0), (rectX, rectY, 20, 75))

    pygame.draw.rect(screen, (60, 180, 0), (rect2X, rect2Y, 20, 75))
    pygame.display.update()


