import pygame
import sys

# Global setup
pygame.init()
pygame.display.set_caption("Template")
screen = pygame.display.set_mode((1000, 600))


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


main()
