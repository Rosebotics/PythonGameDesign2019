# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys

screenSize = (640, 480)
backgroundColor = (234, 19, 210)
circleColor = (0, 129, 9)
circleRadius = 20

rectY = 100
rectSpeed = 1


pygame.init()
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
while True:
     clock.tick(60)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()

     # fill background color
     screen.fill((backgroundColor))


     rectY = rectY + rectSpeed
     if rectY > 485:
         rectSpeed = -1
     elif rectY < 0:
        rectSpeed = 1
     print(rectY)



     pygame.draw.circle(screen, circleColor , (300, 150), circleRadius)
     pygame.draw.rect(screen, (255, 255, 0), (600, rectY, 20, 75))



     pygame.display.update()
