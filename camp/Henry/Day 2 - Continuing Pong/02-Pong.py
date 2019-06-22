# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *


class Ball:

    def  __init__(self, screen, x, y, xSpeed, ySpeed, color, radius) -> object:
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
        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= self .screen.get_height():
            self.ySpeed = self.ySpeed * -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collided(self):
        self.xSpeed = self.xSpeed * -1.01





screenSize = (640, 480)
backgroundColor = (0, 0, 200)
# circleColor = (255, 255, 255)
# circleRadius = 20
# circleX = 320
# circleXSpeed = 5
# circleY = 240
# circleYSpeed = 2
rectX = 600
rectX2 = 20
rectY = 100
rectY2 = 100
rectSpeed = 10

pygame.init()
pygame.display.set_caption("pong")
pygame.key.set_repeat(1, 10)

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball(screen, 320, 240, 5, 2, (255, 255, 255), 20)


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
        if pressed_keys [K_w]:
            rectY2 = rectY2 - rectSpeed
        if pressed_keys [K_s]:
            rectY2 = rectY2 + rectSpeed



    collided1 = pygame.Rect(rectX, rectY, 20, 75).collidepoint(ball.x + ball.radius, ball.y)
    collided2 = pygame.Rect(rectX2, rectY2, 20, 75).collidepoint(ball.x - ball.radius, ball.y)
    if collided1 or collided2:
        ball.collided()



    # fill background before drawing
    screen.fill(backgroundColor)

    ball.move()
    ball.draw()

    # pygame.draw.circle(screen, circleColor, (int(circleX), int(circleY)), circleRadius)
    pygame.draw.rect(screen, (255, 255, 255), (rectX, rectY, 20, 75))
    pygame.draw.rect(screen, (255, 255, 255), (rectX2, rectY2, 20, 75))

    pygame.display.update()
