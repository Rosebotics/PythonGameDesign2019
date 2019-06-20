# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import random

import pygame
import sys
from pygame.locals import *


def draw_text(screen, text, position):
    font = pygame.font.SysFont('Arial', 16)
    textSurface = font.render(text, True, (255, 255, 255))
    rect = textSurface.get_rect()
    rect.center = position
    screen.blit(textSurface, rect)


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

        if(self.x - self.radius) <= 0 or (self.x + self.radius) >= self.screen.get_width():
           self.xSpeed = self.xSpeed * -1
        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= self.screen.get_height():
            self.ySpeed = self.ySpeed * -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def collided(self):
         self.xSpeed = self.xSpeed * -1






screenSize = (640, 480)
backgroundColor = (0, 0, 0)
#CircleColor = (255, 255, 255)
#CircleRadius = 20

rectY = 100
rect2y = 100
#circleX = 320
#circleY = 240
score1 = 0
score2 = 0
#circleXSpeed = 5
#circleYSpeed = 2
rectx = 600
rect2x = 40

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball(screen, 320, 240, 5, 2, (255, 255, 255), 20)
balls = [ball]

while True:
    clock.tick(60)
    if score1 == 10:
        continue
    if score2 == 10:
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY - 5
        if pressed_keys[K_DOWN]:
            rectY = rectY + 5
        if pressed_keys[K_w]:
            rect2y = rect2y - 5
        if pressed_keys[K_s]:
            rect2y = rect2y + 5
        if ball.x >= screen.get_width() - ball.radius:
            ball.xSpeed = -5
            score1 = score1 + 1
        if ball.x <= ball.radius:
            circleXSpeed = 5
            score2 = score2 + 1

    # fill background before drawing
    screen.fill(backgroundColor)
    draw_text(screen, str(score1), (320,100))

    toadd = []
    for ball in balls:

      ball.move()
      ball.draw()

      collided1 = pygame.Rect(rectx, rectY, 20, 75).collidepoint(ball.x + ball.radius, ball.y)
      collided2 = pygame.Rect(rect2x, rect2y, 20, 75).collidepoint(ball.x - ball.radius, ball.y)

      if collided1 or collided2:
            ball.collided()

            if collided1:
                toadd.append(Ball(screen,ball.x, ball.y, -random.randint(2,6), random.randint(1,3), (255, 255, 255), 20))
            if collided2:
                toadd.append(Ball(screen,ball.x, ball.y, random.randint(2,6), random.randint(1,3), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 20))
    for ball in toadd:
        balls.append(ball)
    #rect1
    pygame.draw.rect(screen, (255, 0, 0), (rectx, rectY, 20, 75))
    #rect2
    pygame.draw.rect(screen, (255, 0, 0), (rect2x, rect2y, 20, 75))

    pygame.display.update()
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
