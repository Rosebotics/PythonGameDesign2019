

screensize = (640, 488)
backgroundcolor = (255, 0, 0)
circlecolor = (255, 255, 255)
circleradius = 20
pygame.init()
screen = pygame.display.set_mode(screensize)

rectY = 100
rectspeed = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # remember to fill backround BEFORE drawing
    screen.fill(backgroundcolor)

    pygame.draw.circle(screen, circlecolor, (300, 350), circleradius)
    pygame.draw.rect(screen, (255, 255, 0), (600, rectY, 20, 75))

    rectY = rectY + rectspeed
    if rectY > 480:
        rectspeed = -2
    elif rectY < 0:
        rectspeed =2


    pygame.display.update()
# TODO: Copy all of your   04-Drawing.py   program and put it below this comment.
import pygame
import sys