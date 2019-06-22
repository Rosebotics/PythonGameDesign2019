import pygame, sys, random, time
from pygame.locals import *

def play_sound(laser):
            pygame.mixer.music.load("Laser-SoundBible.com-602495617.mp3")
            pygame.mixer.music.play(0)

class Missile:
    def __init__(self, screen, x):
        # TODO: Save the screen into a field
        self.screen = screen
        # TODO: Save the x into a field
        self.x = x
        # TODO: Set the y to 591 as a field (which is just above the fighter)
        self.y = 591
        # TODO: Set a field called exploded to False
        self.exploded = False

    def move(self):
        # TODO: Move the missile up 5
        self.y = self.y - 5

    def draw(self):
        # DONE: Draw a red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (100, 100, 255), (self.x, self.y), (self.x, self.y + 15), 4)

class enemyMissile:
    def __init__(self, screen, x, y):
        # TODO: Save the screen into a field
        self.screen = screen
        # TODO: Save the x into a field
        self.x = x
        # TODO: Set the y to 591 as a field (which is just above the fighter)
        self.y = y
        # TODO: Set a field called exploded to False
        self.exploded = False

    def move(self):
        # TODO: Move the missile up 5
        self.y = self.y + 5

    def draw(self):
        # DONE: Draw a red line from x, y that is 8 pixels in height
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 15), 4)


class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("ship.png").convert()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.missiles = []
        self.dead = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        play_sound("Laser-SoundBible.com-602495617.mp3")
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

        self.image = pygame.image.load("enemyship1.png").convert()
        self.height = 70
        self.width = 70
        self.image2 = pygame.transform.scale(self.image, (self.width, self.height))

        self.image.set_colorkey((0, 0, 0))
        self.original_x = x
        self.speed = level * 0.5 + 0.5
        self.enemyMissiles = []
        self.badGuysHitEdge = False


    def move(self):
        self.x = self.x + self.speed
        if self.x == 825 or self.x == 0:
            self.badGuysHitEdge = True
        if random.randint(1, 1000) == 1:
            self.enemyMissiles.append(enemyMissile(self.screen, self.x + 35, self.y))

    def advance(self):
        self.y = self.y + 30
        self.speed = self.speed * -1
        self.x = self.x + self.speed
        self.badGuysHitEdge = False

    def draw(self):
        self.screen.blit(self.image2, (self.x, self.y))

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 70, 45).collidepoint(missile.x, missile.y)

    def remove_exploded_missiles(self):
        for k in range(len(self.enemyMissiles) - 1, -1, -1):
            if self.enemyMissiles[k].exploded or self.enemyMissiles[k].y < 0:
                del self.enemyMissiles[k]


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(10):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    def advance(self):
        for badguy in self.badguys:
            badguy.advance()

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

level = 1

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((900, 650))

    # done: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 4
    # done: Create an EnemyFleet object (called enemy) with the screen and enemy_rows
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    # done: Create a Fighter (called fighter) at location  320, 590
    fighter = Fighter(screen, 320, 550)
    game_over = False

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # done: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()
        # done: If K_LEFT is pressed move the fighter left 3
        if pressed_keys[K_LEFT] and fighter.x > 0:
            fighter.x = fighter.x - 3
        # done: If K_RIGHT is pressed move the fighter right 3
        if pressed_keys[K_RIGHT] and fighter.x < 800:
            fighter.x = fighter.x + 3
        # done: Draw the fighter
        fighter.draw()
        # done: Move the enemy
        enemy_fleet.move()
        for badguy in enemy_fleet.badguys:
            if badguy.badGuysHitEdge == True:
                enemy_fleet.advance()
                break
        # done: Draw the enemy
        enemy_fleet.draw()
        # done: For each missile in the fighter missiles
        for missile in fighter.missiles:
                missile.move()
                missile.draw()
        # done: Move the missile
        # done: Draw the missile

        # done: For each badguy in the enemy badguys
        for badguy in enemy_fleet.badguys:
            for enemyMissile in badguy.enemyMissiles:
                if fighter.hit_by(enemyMissile):
                    fighter.dead = True
                    enemyMissile.exploded = True
                else:
                    enemyMissile.move()
                    enemyMissile.draw()

            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    badguy.dead = True
                    missile.exploded = True

        #     done: For each missle in the fighter missiles
        #         done: If the badguy is hit by the missle
        #             done: Mark the badguy as dead = True
        #             done: Mark the missile as exploded = True


        # TODO: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missiles()
        # TODO: Use the enemy to remove dead badguys
        enemy_fleet.remove_dead_badguys()


        # TODO: If the enemy is_defeated
        if enemy_fleet.is_defeated:
            enemy_fleet = EnemyFleet(screen, enemy_rows)
            level = level + 1
        for badguy in enemy_fleet.badguys:
            if badguy.y > 545:
                game_over = True
        #     TODO: Create a new enemy with the screen and enemy_rows
        if badguy.y > 545 or fighter.dead:
            game_over = True

        if game_over:
            screen.fill((0, 0, 0))
            game_over_image = pygame.image.load("gameover.png").convert()
            pygame.transform.scale(game_over_image, (900, 650), screen)
        pygame.display.update()


main()
