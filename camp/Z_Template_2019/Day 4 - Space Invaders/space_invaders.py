import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   exploded to False.
        pass

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        pass

    def draw(self):
        # Draw a horizontal, 1-pixel thick, 8 pixels long, red line on the screen,
        # where the line starts at the current position of this Missile.
        pass

class Fighter:
    def __init__(self, screen, x, y):
        # TODO 7:  See your Ball class to see how to:
        #   TODO: Store the  screen  x  y   in
        #   TODO:   self.screen   self.x   self.y
        self.screen = screen
        self.x = x
        self.y = y

        # TODO 8:  See the example on images (on the whiteboard) to see how to:
        #   TODO: Load the file  "fighter.png"  as the image. and set its colorkey to white.
        self.image = pygame.image.load("fighter.png").convert()
        self.image.set_colorkey((255, 255, 255))

        # Set   self.missiles   to the empty list.


    def draw(self):
        # TODO 9:  See the example on images (on the whiteboard) to see how to:
        #   TODO:  Draw this Fighter, using its image at its current (x, y) position.
        #   HINT:  you will be using   self.image   and   self.x   and   self.y.
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        # Construct a new Missile 50 pixels to the right of this Fighter.
        # Append that Missile to this Fighter's list of Missile objects.
        pass

    def remove_exploded_missles(self):
        # for k in range(len(self.missiles) - 1, -1, -1):
            # if self.missiles[k].exploded or self.missiles[k].y < 0:
                # del self.missiles[k]
        pass


class Badguy:
    def __init__(self, screen, x, y):
        # TODO 13:  See your Fighter class to see how to:
        #   TODO: Store the  screen  x  y   in
        #   TODO:   self.screen   self.x   self.y
        #   TODO: Load the file  "badguy.png"  as the image. and set its colorkey to BLACK (not white).
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png").convert()
        self.image.set_colorkey((0, 0, 0))

        # TODO 19: Make a self.speed and set it to 1.
        self.xspeed = 1

        # Set   dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        pass

    def move(self):
        # TODO 20:  See how your Ball moved in your Pong game to:
        #   TODO: Make this move per its self.xspeed.
        self.x = self.x + self.xspeed
        
        #   TODO: Change its self.speed appropriately if self.x is negative or too big.
        #
        # if self.x < 0 or self.x > 1050:
        #     self.xspeed = self.xspeed * -1

    def draw(self):
        # TODO 14:  See the example from your Fighter class to:
        #   TODO: Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, missile):
        # Return True if a 70x45 rectangle at this Badguy's current position
        #   collides with a point the given missile's current position.
        # Return False otherwise.
        pass


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # TODO 15: Ask your teacher to explain the next lines of code.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20))

    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        pass

    def move(self):
        # TODO 21:  See how you made each Badguy   draw   (in the  draw  method just below this method) to:
        #   TODO: Loop through   self.badguys   and   move each badguy.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # TODO 16:  See how you used your  ballist   to draw each Ball that you had, to (here):
        #   TODO: Loop through   self.badguys   and   draw each badguy.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


class Scoreboard:
    def __init__(self, screen, x, y):
        # TODO: Save the screen to a field
        # TODO: Save the x and y to fields
        # TODO: Initialize a score field with a value of 0
        # TODO: Create a font object with a 30 point font (this is new)
        pass


    def draw(self):
        # TODO: Convert the score number into a string called as_text using the format "Score: " + number
        # TODO: Using the font object convert the string into an image that can be placed onto the screen, call it as_image
        # TODO: Using the screen blit as_image onto the location self.x and self.y
        pass


def main():
    # TODO 2:  See your Pong program for how to:
    #  TODO: Initialize pygame.
    #  TODO: make a Clock.
    #  TODO: Set the caption to a title you like, e.g. ":0 SPACE INVADERS!!!!! :0"
    #  TODO: Set the   screen  by setting its   mode   to have size   1040 x 1050.
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(":0 SPACE INVADERS!!!!! :0")
    screen = pygame.display.set_mode((1040, 1050))


    # TODO 10: See how you made a Ball in your Pong game to:
    #  TODO: Create a Fighter (called fighter) at location  320, 590.
    fighter = Fighter(screen, 320, 590)

    # TODO 17: Set    enemy_rows    to an initial value of 3
    #   TODO: and set   enemy   to an   EnemyFleet(screen, enemy_rows).
    enemy_rows = 3
    enemy = EnemyFleet(screen, enemy_rows)

    # TODO: Create a Scoreboard, called scoreboard, using the screen at location 5, 5

    # TODO 3:  See the example from your Pong game to:
    #   TODO: Make a   while True:    loop.
    while True:

        # TODO 4: See the example from your Pong game to (INSIDE your  while True:  loop):
        #   TODO: Fill the screen with black, which is (0, 0, 0).
        screen.fill((0, 0, 0))

        # TODO 6:  See the example from your Pong game to (still INSIDE your  while True:  loop):
        #   TODO: Make the clock tick 60 units.
        #   TODO: Add a   for event in pygame.event.get():  loop
        #   TODO: whose insides checks if the event.type == pygame.QUIT
        #   TODO: and if so, does a   sys.exit()
        #   NOTE: At this point your game should show a black screen and you can click the X to stop the game.
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # TODO 12:  See how you used the arrow keys to move the paddles in your Pong game to:
        #   TODO: Set   pressed_keys   to the keys that have been pressed.
        #   TODO: If K_LEFT is pressed and   fighter.x > -50  , move the fighter left 3 (by using  fighter.x)
        #   TODO: If K_RIGHT is pressed and  fighter.x < 590  , move the fighter right 3 (by using fighter.x).
        #   NOTE: At this point you should be able to move the figher left and right.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and fighter.x > -50:
            fighter.x = fighter.x - 5
        if pressed_keys[pygame.K_RIGHT] and fighter.x < 590:
            fighter.x = fighter.x + 5


        # pressed_keys = pygame.key.get_pressed()
        # # TODO: If the event type is KEYDOWN and pressed_keys[K_SPACE} is True, then fire a missile
        #

        # TODO 11: See your Pong game for how you drew the Ball to:
        #  TODO: Draw the fighter.
        #  NOTE: At this point your fighter should appear on the screen.
        fighter.draw()
        #
        # TODO 22. See how you made your fighter draw (in the line above) to:
        #   TODO: Make the  enemy  move.
        #   NOTE: At this time, the enemy should move to the right slowly.
        enemy.move()

        # TODO 18: Use the example above for how you drew your fighter to:
        #   TODO: Draw the enemy.
        #   NOTE: At this time the enemy fleet should appear on your screen.
        enemy.draw()

        # # TODO: Draw the scoreboard
        #
        #
        # # TODO: For each missle in the fighter missiles
        # # TODO: Move the missle
        # # TODO: Draw the missle
        #
        #
        # # TODO: For each badguy in the enemy badguys
        # #     TODO: For each missle in the fighter missiles
        # #         TODO: If the badguy is hit by the missle
        # #             TODO: Mark the badguy as dead = True
        # #             TODO: Mark the missile as exploded = True
        # #             TODO: Increment the score of the scoreboard by 100
        #
        # # TODO: Use the fighter to remove exploded missiles
        # # TODO: Use the enemy to remove dead badguys
        #
        #
        # # TODO: If the enemy id_defeated
        # #     TODO: Increment the enemy_rows
        # #     TODO: Create a new enemy with the screen and enemy_rows
        #
        # # TODO: Check to see if their is a badguy whose y > 545.  If so, the game is over and you should:
        # #     TODO: Display a "game over" image, and
        # #     TODO: "break" out of the game loop (to stop the program).
        #

        # TODO 5: See your Pong game for how to:
        #   TODO: Update the pygame display.
        #   NOTE:  Your screen will "lock up" until you have done the NEXT TODO.
        pygame.display.update()

# TODO 1: Call main.
main()

