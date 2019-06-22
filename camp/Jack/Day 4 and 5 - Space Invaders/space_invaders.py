import pygame, sys, random, time
from pygame.locals import *

def draw_text(screen, text, position, color, font='Arial', size=50):
    font = pygame.font.SysFont(font, size)
    textSurface = font.render(text, True, color)
    rect = textSurface.get_rect()
    rect.center = position
    screen.blit(textSurface, rect)

class Missile:
    def __init__(self, screen, x):
        # DONE: Save the screen into a field
        self.screen = screen
        # DONE: Save the x into a field
        self.x = x
        # DONE: Set the y to 591 as a field (which is just above the fighter)
        self.y = 591
        # DONE: Set a field called exploded to False
        self.exploded = False

    def move(self):
        self.y = self.y - 5
        # DONE: Move the missile up 5


    def draw(self):
        pygame.draw.line(self.screen, (255, 0, 0), (self.x, self.y), (self.x, self.y + 8), 1)
        # DONE: Draw a red line from x, y that is 8 pixels in height



class EnemyMissile:
    def __init__(self, screen, x, y):
        # DONE: Save the screen into a field
        self.screen = screen
        # DONE: Save the x into a field
        self.x = x
        # DONE: Set the y to 591 as a field (which is just above the fighter)
        self.y = y
        # DONE: Set a field called exploded to False
        self.exploded = False

    def move(self):
        self.y = self.y + 3
        # DONE: Move the missile up 5


    def draw(self):
        pygame.draw.line(self.screen, (255, 0, 255), (self.x, self.y), (self.x, self.y + 8), 1)
        # DONE: Draw a red line from x, y that is 8 pixels in height



class Fighter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("fighter.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.missiles = []
        self.dead = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.missiles.append(Missile(self.screen, self.x + 50))

    def remove_exploded_missiles(self):
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].exploded or self.missiles[k].y < 0:
                del self.missiles[k]

    def hit_by(self, missile):
        return pygame.Rect(self.x, self.y, 100, 100).collidepoint(missile.x, missile.y)



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
        self.missiles = []
        self.yspeed = 15

    def move(self):
        self.x = self.x + self.speed
        if self.x > self.original_x + 100 or self.x < self.original_x - 100:
            self.speed = self.speed * -1
            self.y = self.y + self.yspeed
        if random.randint(1,1000) <2:
            self.missiles.append(EnemyMissile(self.screen, self.x, self.y))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

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
    pygame.display.set_caption("Space Invaders")
    pygame.key.set_repeat(1, 70)
    screen = pygame.display.set_mode((640, 650))

    # DONE: Set    enemy_rows    to an initial value of 3.
    enemy_rows = 3
    enemy_fleet = EnemyFleet(screen, enemy_rows)
    fighter = Fighter(screen, 320, 590)
    game_over = False
    damage = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # DONE: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
            if pressed_keys[K_SPACE] and event.type == KEYDOWN:
                fighter.fire()
            if event.type == QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        pressed_keys = pygame.key.get_pressed()

        # DONE: If K_LEFT is pressed move the fighter left 3
        if pressed_keys[K_LEFT]:
            fighter.x = fighter.x - 3
        if fighter.x < -50:
            fighter.x = -50
        if fighter.x > 588:
            fighter.x = 588
        # DONE: If K_RIGHT is pressed move the fighter right 3
        if pressed_keys[K_RIGHT]:
            fighter.x = fighter.x + 3
        # DONE: Draw the fighter
        fighter.draw()

        # DONE: Move the enemy
        enemy_fleet.move()
        # DONE: Draw the enemy
        enemy_fleet.draw()

        # DONE: For each missile in the fighter missiles
        for missile in fighter.missiles:
        # DONE: Move the missile
            missile.move()
        # DONE: Draw the missile
            missile.draw()

        # DONE: For each badguy in the enemy badguys
        # DONE: For each missile in the fighter missiles
        # DONE: If the badguy is hit by the missile
        for badguy in enemy_fleet.badguys:
            for enemyMissile in badguy.missiles:
                if fighter.hit_by(enemyMissile):
                    damage = damage + 1
                    print(damage)
                    enemyMissile.exploded = True
                if damage > 9:
                    fighter.dead = True
                else:
                    enemyMissile.move()
                    enemyMissile.draw()
            badguy.remove_exploded_missiles()
            for enemyMissile in badguy.missiles:
                enemyMissile.move()
                enemyMissile.draw()
            for missile in fighter.missiles:
                if badguy.hit_by(missile):
                    # DONE: Mark the badguy as dead = True
                    # DONE: Mark the missile as exploded = True
                    badguy.dead = True
                    missile.exploded = True

        # DONE: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missiles()
        # DONE: Use the enemy to remove dead badguys
        enemy_fleet.remove_dead_badguys()

        # DONE: If the enemy is_defeated
        if enemy_fleet.is_defeated:
            # DONE: Increment the enemy_rows
            # DONE: Create a new enemy with the screen and enemy_rows
            enemy_rows = enemy_rows + 1
            enemy_fleet = EnemyFleet(screen, enemy_rows)

        if enemy_rows == 12:
            game_over = True
            screen.fill((0,0,0))
            draw_text(screen, 'You Won',(320, 325), (255, 255, 255))
            pygame.display.update()

        draw_text(screen, "Damage:" + str(damage), (100,40), (255, 255, 255))

        if not game_over:
            pygame.display.update()
            for badguy in enemy_fleet.badguys:
                if badguy.y > 545 or fighter.dead:
                    game_over = True
                    game_over_image = pygame.image.load("gameover.png").convert()
                    screen.blit(game_over_image, (170, 200))
                    pygame.display.update()


main()
