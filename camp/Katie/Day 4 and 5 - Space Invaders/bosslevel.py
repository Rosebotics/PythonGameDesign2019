import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        # Done: Save the screen into a field
        self.screen = screen
        # Done: Save the x into a field
        self.x = x
        # Done: Set the y to 591 as a field (which is just above the fighter)
        self.y = 591
        # Done: Set a field called exploded to False
        self.exploded = False
        pass

    def move(self):
        # Done: Move the missile up 5
        self.y = self.y - 5
        pass

    def draw(self):
        # Done: Draw a red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (255, 255, 100), (self.x, self.y), (self.x, self.y + 10), 2)
        pass

class EnemyMissile:
    def __init__(self, screen, x, y):
        # Done: Save the screen into a field
        self.screen = screen
        # Done: Save the x into a field
        self.x = x
        # Done: Set the y to 591 as a field (which is just above the fighter)
        self.y = y
        # Done: Set a field called exploded to False
        self.exploded = False
        pass

    def move(self):
        # Done: Move the missile up 5
        self.y = self.y + 5
        pass

    def draw(self):
        # Done: Draw a   red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (255, 100, 100), (self.x, self.y), (self.x, self.y + 10), 2)
        pass

class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("fighter.png").convert()
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
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)

    def remove_exploded_missles(self):
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
        self.speed = 15
        self.missiles = []

    def move(self):
        self.x = self.x + self.speed
        if self.x > self.original_x + 100 or self.x < self.original_x - 100:
            self.speed = self.speed * -1
            self.y = self.y + 50
        if random.randint(1, 1000) < 2:
            self.missiles.append(EnemyMissile(self.screen, self.x, self.y))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)

    def remove_exploded_missles(self):
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
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((640, 650))

    # Done: Set enemy_rows to an initial value of 3
    enemy_rows = 3
    # Done: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # Done: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 590)
    game_over = False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # Done: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()

            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # Done: If K_LEFT is pressed move the fighter left 3
        if pressed_keys[K_LEFT] and fighter.x > -50:
            fighter.x = fighter.x - 3
        # Done: If K_RIGHT is pressed move the fighter right 3
        if pressed_keys[K_RIGHT] and fighter.x < 590:
            fighter.x = fighter.x + 3
        # Done: Draw the fighter
        fighter.draw()

        # Done: Move the enemy
        enemy_fleet.move()
        # Done: Draw the enemy
        enemy_fleet.draw()

        # TODO: For each missle in the fighter missiles
        for missile in fighter.missiles:
        # Done: Move the missle
            missile.move()
        # Done: Draw the missle
            missile.draw()
        # Done: For each badguy in the enemy badguys
        # Done: For each missle in the fighter missiles
        # Done: If the badguy is hit by the missle
        # Done: Mark the badguy as dead = True
        # Done: Mark the missile as exploded = True
        for badguy in enemy_fleet.badguys:
            for EnemyMissile in badguy.missiles:
                if fighter.hit_by(EnemyMissile):
                    fighter.dead = True
                    EnemyMissile.exploded = True
                else:
                    EnemyMissile.move()
                    EnemyMissile.draw()
            badguy.remove_exploded_missles()
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.dead = True
                    missile.exploded = True



        # Done: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missles()
        # Done: Use the enemy to remove dead badguy
        enemy_fleet.remove_dead_badguys()
        # TODO: If the enemy is_defeated
        if enemy_fleet.is_defeated:
            enemy_rows = enemy_rows + 1
            enemy_fleet = EnemyFleet(screen, enemy_rows)


        # TODO: Increment the enemy_rows
        # TODO: Create a new enemy with the screen and enemy_rows

        if not game_over:
            pygame.display.update()
            for badguy in enemy_fleet.badguys:
                if badguy.y > 545 or fighter.dead:
                    game_over = True
                    game_over_image = pygame.image.load("gameover.png").convert()
                    screen.blit(game_over_image, (170, 200))
                    pygame.display.update()

main()
