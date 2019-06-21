import pygame, sys, random, time
from pygame.locals import *


class Nolan:
    def __init__(self, screen, x):
        self.screen = screen

        # TODO: Save the x into a field
        self.x = x
        # TODO: Set the y to 591 as a field (which is just above the fighter)
        self.y = 591
        # TODO: Set a field called exploded to False
        self.exploded = False
        pass
    def move(self):
        # TODO: Move the missile up 5
       self.y = self.y - 5
    def draw(self):
        # TODO: Draw a red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 7),2)

class Fighter2:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("fighter2.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.missiles = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y - 50))

    def fire(self):
        self.missiles.append(Nolan(self.screen, self.x + 100))

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        self.dead = False
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_x = x
        self.speed = 2

    def move(self):
        self.x = self.x + self.speed
        if self.x > self.original_x + 100 or self.x < self.original_x - 100:
            self.speed = self.speed * -1
            self.y = self. y + 15

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, Nolan):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(Nolan.x, Nolan.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    @property
    def is_defeated(self):
        return len(self.badguys) == 0

    def move(self):
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Invaders")
    pygame.key.set_repeat(1, 70)
    screen = pygame.display.set_mode((640, 650))

    # DONE: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # DONE: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    # DONE: Create a Fighter (called fighter) at location  320, 590
    fighter2 = Fighter2 (screen, 320, 590)
    game_over = False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # TODO: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter2.fire()
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # done: If K_LEFT is pressed move the fighter left
        if pressed_keys[K_LEFT]:
            fighter2.x = fighter2.x - 5
        # done: If K_RIGHT is pressed move the fighter right
        if pressed_keys[K_RIGHT]:
            fighter2.x = fighter2.x + 5
        # done: Draw the fighter
        fighter2.draw()
        # done: Move the enemy
        enemy_fleet.move()
        # done: Draw the enemy
        enemy_fleet.draw()

        for Nolan in fighter2.missiles:
            Nolan.move()
        # done: Draw the missle
            Nolan.draw()
        # done: For each badguy in the enemy badguys
        for badguy in enemy_fleet.badguys:
        # done: For each missle in the fighter missiles

            for Nolan in fighter2.missiles:
        # done: If the badguy is hit by the missle
                if badguy.hit_by(Nolan):
                    badguy.dead = True
                    Nolan.exploded = True



        #             TODO: Mark the badguy as dead = True
        #             TODO: Mark the missile as exploded = True


        # done: Use the fighter to remove exploded missiles
        fighter2.remove_exploded_missiles()

        # done: Use the enemy to remove dead badguys
        enemy_fleet.remove_dead_badguys()


        # TODO: If the enemy is_defeated
        #     TODO: Increment the enemy_rows
        #     TODO: Create a new enemy with the screen and enemy_rows
        if enemy_fleet.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy_fleet = EnemyFleet (screen, enemy_rows)





        if not game_over:
            pygame.display.update()
            for badguy in enemy_fleet.badguys:
                if badguy.y > 545:
                    game_over = True
                    game_over_image = pygame.image.load("gameover.png").convert()
                    screen.blit(game_over_image,(170, 200))
                    pygame.display.update()


main()
