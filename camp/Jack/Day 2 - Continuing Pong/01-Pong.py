# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys



class Ball:

    def _init_(self, screen, x, y, xSpeed, ySpeed, color, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color
        self.radius = radius



















from pygame.locals import *

screenSize = (640, 480)
backgroundColor = (0, 0, 0)
CircleColor = (255, 255, 255)
CircleRadius = 20

rectY = 100
rect2y = 100
circleX = 320
circleY = 240
score1 = 0
score2 = 0
circleXSpeed = 5
circleYSpeed = 2
rectx = 600
rect2x = 40

pygame.init()
pygame.display.set_caption("Pong!")
pygame.key.set_repeat(1, 10)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
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
        if circleX > 640:
            circleXSpeed = -5
            score1 = score1 + 1
        if circleX < 0:
            circleXSpeed = 5
            score2 = score2 + 1

    # fill background before drawing
    screen.fill(backgroundColor)

    circleX = circleX + circleXSpeed
    if circleX > 640 or circleX < 0:
        circleXSpeed = circleXSpeed * -1
    circleY = circleY + circleYSpeed
    if circleY > 480 or circleY < 0:
        circleYSpeed = circleYSpeed * -1

    collided1 = pygame.Rect(rectx, rectY, 20, 75).collidepoint(circleX + CircleRadius, circleY)
    collided2 = pygame.Rect(rect2x, rect2y, 20, 75).collidepoint(circleX - CircleRadius, circleY)

    if collided1 or collided2:
        circleXSpeed = circleXSpeed * -1.02

    pygame.draw.circle(screen, CircleColor, (int(circleX), int(circleY)), CircleRadius)
    #rect1
    pygame.draw.rect(screen, (255, 0, 0), (rectx, rectY, 20, 75))
    #rect2
    pygame.draw.rect(screen, (255, 0, 0), (rect2x, rect2y, 20, 75))

    pygame.display.update()
# TODO: Copy all of your   05-Animation.py   program and put it below this comment.
