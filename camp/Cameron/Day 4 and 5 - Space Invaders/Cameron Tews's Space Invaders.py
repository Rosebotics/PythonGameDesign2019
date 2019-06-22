import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x

        self.y = 591
        self.exploded = False
    def move(self):
        self.y = self.y -15

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 255), (self.x, self.y), (self.x, self.y + 30), 1)

class EnemyMissile:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x

        self.y = y
        self.exploded = False
    def move(self):
        self.y = self.y + 1

    def draw(self):
        pygame.draw.line(self.screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + 30), 1)



class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 140
        self.height = 80
        self.screen = screen
        self.image = pygame.image.load("spitfire.png").convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.dead = False
        self.missiles = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.missiles.append(Missile(self.screen, self.x + 50))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 100, 100).collidepoint(missile.x, missile.y)

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
        self.width = 70
        self.height = 70
        self.image = pygame.image.load("STUKA.png").convert()
        self.image2 = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_colorkey((255, 255, 255))
        self.original_x = x
        self.speed = 2
        self.missiles = []

    def move(self):
        self.x = self.x + self.speed
        if self.x > self.original_x + 100 or self.x < self.original_x - 100:
            self.speed = self.speed * -1
            self.y = self.y + 15
        if random.randint(1, 650) < 2:
            self.missiles.append(EnemyMissile(self.screen, self.x, self.y))

    def draw(self):
        self.screen.blit(self.image2, (self.x, self.y))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]


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
    pygame.display.set_caption("Cameron Tews's Battle of Britan")
    screen = pygame.display.set_mode((640, 650))


    enemy_rows = 3
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    fighter = Fighter(screen, 320, 590)
    game_over = False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            fighter.x = fighter.x - 15
        if pressed_keys[K_RIGHT]:
            fighter.x = fighter.x + 15

        fighter.draw()


        enemy_fleet.move()
        enemy_fleet.draw()

        for missile in fighter.missiles:

            missile.move()
            missile.draw()

        for badguy in enemy_fleet.badguys:
            for EnemyMissile in badguy.missiles:
                if fighter.hit_by(EnemyMissile):
                    fighter.dead = True
                else:
                    EnemyMissile.move()
                    EnemyMissile.draw()
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.dead = True
                    missile.exploded = True

        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

        if enemy_fleet.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy_fleet =EnemyFleet(screen, enemy_rows)


        if not game_over:
            pygame.display.update()
            for badguy in enemy_fleet.badguys:
                if badguy.y > 545 or fighter.dead:
                    game_over = True
                    game_over_image = pygame.image.load("end of game.jpg").convert()
                    screen.blit(game_over_image, (170, 200))
                    pygame.display.update()



main()
