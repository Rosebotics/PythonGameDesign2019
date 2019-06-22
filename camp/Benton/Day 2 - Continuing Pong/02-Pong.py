# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
import pygame
import sys
from pygame.locals import *

#score = 0

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
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collided(self):
        if collided1:
            self.xSpeed = -5
            #0score = score + 1
        if collided2:
            self.xSpeed = 5
            #score = score + 1


screenSize = (640, 480)
backgroundColor = (0, 0, 255)
#dotColor = (255, 255, 255)
#circleRadius = 20
#circleX = 320
#circleY = 240
#ballXSpeed = 5
#ballYSpeed = 2

rectY = 360
rect2Y = 40
rectSpeed = 5

pygame.init()
pygame.key.set_repeat(1,10)

# rect 1 600 rect 2 40

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

ball = Ball(screen, 320, 240, 5, 2, (255, 255, 255), 20)

while True:
    clock.tick(60)
    pygame.display.set_caption("Pong")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            rectY = rectY -rectSpeed
        if pressed_keys[K_DOWN]:
            rectY = rectY + rectSpeed
        if pressed_keys[K_w]:
            rect2Y = rect2Y - rectSpeed
        if pressed_keys[K_s]:
            rect2Y = rect2Y + rectSpeed

    # fill background before drawing

    screen.fill(backgroundColor)

    ball.move()
    ball.draw()

    collided1 = pygame.Rect(600, rectY, 20, 75).collidepoint(ball.x + ball.radius, ball.y)
    collided2 = pygame.Rect(20, rect2Y, 20, 75).collidepoint(ball.x - ball.radius, ball.y)

    if collided1 or collided2:
        ball.collided()

    pygame.draw.rect(screen, (255, 255, 255), (600, rectY, 20, 75))
    # rect 1
    pygame.draw.rect(screen, (255, 255, 255), (20, rect2Y, 20, 75))
    # rect 2
    pygame.display.update()
