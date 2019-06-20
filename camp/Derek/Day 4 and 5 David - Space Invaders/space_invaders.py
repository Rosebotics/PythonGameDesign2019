import pygame, sys, random, time
from pygame.locals import *


class Missile:
    def __init__(self, screen, x, y):
        pass
        # TODO 25:  See your Fighter class to see how to:
        #   TODO: Store the  screen  x  y   in
        #   TODO:   self.screen   self.x   self.y

        # TODO 33: Set   self.is_exploded   to False (the missile starts out unexploded).

    def move(self):
        pass
        # TODO 27:  Make self.y   5 smaller   than it was (which will cause the Missile to move UP).

    def draw(self):
        pass
        # TODO 26:  See the example on the whiteboard to:
        #   TODO: Draw a horizontal, 1-pixel thick, 8 pixels long, red line on the screen,
        #   TODO: where the line starts at the current position of this Missile.


class Fighter:
    def __init__(self, screen, x, y):
        pass
        # TODO 7:  See your Ball class to see how to:
        self.screen = screen
        self.x = x
        self.y = y
        #   TODO: Store the  screen  x  y   in
        #   TODO:   self.screen   self.x   self.y

        # TODO 8:  See the example on images (on the whiteboard) to see how to:
        #   TODO: Load the file  "fighter.png"  as the image. and set its colorkey to white.
        self.image = pygame.image.load("fighter.png").convert()
        self.image.set_colorkey((255,255,255))

        # TODO 28:  Set   self.missiles   to the empty list, that is, to   []


    def draw(self):
        pass
        # TODO 9:  See the example on images (on the whiteboard) to see how to:

        self.screen.blit(self.image,(self.x,self.y))
        #   TODO:  Draw this Fighter, using its image at its current (x, y) position.
        #   HINT:  you will be using   self.image   and   self.x   and   self.y.

        # TODO 30:  See how you looped through each badguy in the  draw  method of EnemyFleet to:
        #   TODO: Loop through   self.missiles   and   draw each missile and also move each missile.

    def fire(self):
        pass
        # TODO 29:  See how you appended Ball objects to your balllist in Pong to:
        #   TODO: Construct a new Missile 50 pixels to the right of this Fighter and at y position 591.
        #   TODO: Append that Missile to self.missiles.

    def remove_exploded_missiles(self):
        # TODO 34:  Ask your teacher to explain the lines below.
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].is_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y):
        pass

        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png").convert()
        self.image.set_colorkey((0,0,0))
        # TODO 13:  See your Fighter class to see how to:


        #   TODO: Store the  screen  x  y   in
        #   TODO:   self.screen   self.x   self.y
        #   TODO: Load the file  "badguy.png"  as the image. and set its colorkey to BLACK (not white).

        # TODO 19: Make a self.speed and set it to 1.
        self.speed = 1

        # TODO 23:  Set    self.original_x    to   self.x.
        #           Set    self.is_dead       to   False.
        self.original_x = self.x
        self.is_dead = False

    def move(self):
        pass
        # TODO 20:  See how your Ball moved in your Pong game to:
        #   TODO: Make this move per its self.xspeed.

        self.x = self.x + self.speed



        # TODO 24: If   self.xspeed > 0  (so the Badguy is moving to the right)
        #          and   self.x  is bigger than   self.original_x + 100, then
        #   TODO: Make the Badguy reverse its direction (by multiplying self.xspeed by -1), and
        #   TODO: Make the Badguy move down 15 (by increasing its self.y by 15).
        # TODO:  Then do similarly if   self.xspeed < 0 (but comparing self.x to   self.original - 100   in that case).
        # NOTE: At this point the enemy fleet should bounce (like the Ball bounced) in the x-direction
        #       and go down a bit when it bounces.
        self.speed = self.speed *-1
        self.y = self.y - 15
    def draw(self):
        pass
        self.screen.blit(self.image,(self.x,self.y))
        # TODO 14:  See the example from your Fighter class to:
        #   TODO: Draw this Badguy, using its image at its current (x, y) position.

    def hit_by(self, missile):
        pass
        # TODO 35:  See the example on the board to see how to:
        #   TODO: Return True if a 70x45 rectangle at this Badguy's current position
        #         collides with a point the given missile's current position.
        #         Return False otherwise.

class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # TODO 15: Ask your teacher to explain the next lines of code.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 200 + (80 * k), 50 * j + 20))

    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        pass

    def move(self):
        pass
        # TODO 21:  See how you made each Badguy   draw   (in the  draw  method just below this method) to:
        #   TODO: Loop through   self.badguys   and   move each badguy.
        for b in self.badguys:
            b.move()

    def draw(self):
        pass
        # TODO 16:  See how you used your  ballist   to draw each Ball that you had, to (here):
        #   TODO: Loop through   self.badguys   and   draw each badguy.

        for b in self.badguys:
            b.draw()





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
    pass
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Invaders of Mars")
    screen = pygame.display.set_mode( (1040,1050))

    # TODO 2:  See your Pong program for how to:
    #  TODO: Initialize pygame.
    #  TODO: make a Clock.
    #  TODO: Set the caption to a title you like, e.g. ":0 SPACE INVADERS!!!!! :0"
    #  TODO: Set the   screen  by setting its   mode   to have size   1040 x 1050.

    # TODO 10: See how you made a Ball in your Pong game to:
    #  TODO: Create a Fighter (called fighter) at location  320, 590.
    fighter = Fighter(screen,320,590)

    # TODO 17: Set    enemy_rows    to an initial value of 3
    #   TODO: and set   enemy   to an   EnemyFleet(screen, enemy_rows).
    enemy_rows = 3
    enemy = EnemyFleet(screen, enemy_rows)

    # TODO: Create a Scoreboard, called scoreboard, using the screen at location 5, 5

    # TODO 3:  See the example from your Pong game to:
    #   TODO: Make a   while True:    loop.
    while True:
        backgroundColor=(0,0,0)
        screen.fill(backgroundColor)


        # TODO 4: See the example from your Pong game to (INSIDE your  while True:  loop):
        #   TODO: Fill the screen with black, which is (0, 0, 0).

        # TODO 6:  See the example from your Pong game to (still INSIDE your  while True:  loop):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #   TODO: Make the clock tick 60 units.
        #   TODO: Add a   for event in pygame.event.get():  loop
        #   TODO: whose insides checks if the event.type == pygame.QUIT
        #   TODO: and if so, does a   sys.exit()
        #   NOTE: At this point your game should show a black screen and you can click the X to stop the game.

        # TODO 12:  See how you used the arrow keys to move the paddles in your Pong game to:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and fighter.x > -0:
            fighter.x=fighter.x-3

        if pressed_keys[K_RIGHT] and fighter.x < 940:
            fighter.x=fighter.x+3





        #   TODO: Set   pressed_keys   to the keys that have been pressed.
        #   TODO: If K_LEFT is pressed and   fighter.x > -50  , move the fighter left 3 (by using  fighter.x)
        #   TODO: If K_RIGHT is pressed and  fighter.x < 590  , move the fighter right 3 (by using fighter.x).
        #   NOTE: At this point you should be able to move the fighter left and right.

        # TODO 31: See how you checked if the K_LEFT key was pressed just above to:
        #   TODO: Checked if pressed_keys[K_SPACE] is True,
        #   TODO: and if so, then fire a missile by using the  fighter.fire()  method.
        #   NOTE: At this point firing missiles should appear when you press the SPACE bar.

        # TODO 11: See your Pong game for how you drew the Ball to:
        #  TODO: Draw the fighter.
        fighter.draw()
        #  NOTE: At this point your fighter should appear on the screen.
        #
        # TODO 22. See how you made your fighter draw (in the line above) to:
        #   TODO: Make the  enemy  move.
        enemy.move()
        #   NOTE: At this time, the enemy should move to the right slowly.

        # TODO 18: Use the example above for how you drew your fighter to:
        #   TODO: Draw the enemy.
        enemy.draw()

        #   NOTE: At this time the enemy fleet should appear on your screen.

        # TODO: Draw the scoreboard

        # TODO 36:  Se your previous examples of   for   loops to see how to:
        #   TODO: For each badguy in enemy
        #     TODO: For each missile in fighter.missiles
        #         TODO: If the badguy is hit by the missile (use the  hit_by  method):
        #             TODO: Set the badguy's   is_dead   to True
        #             TODO: set the missile's  is_exploded to  True
        # At this point, missiles will start exploding the Badguys!

        # TODO 37: Use the fighter to remove exploded missiles
        #  TODO:   Use the enemy to remove dead badguys
        #  HINT:   This requires just 2 lines of code!

        # TODO: Increment the score of the scoreboard by 100

        # TODO: If the enemy id_defeated
        #     TODO: Increment the enemy_rows
        #     TODO: Create a new enemy with the screen and enemy_rows

        # TODO: Check to see if their is a badguy whose y > 545.  If so, the game is over and you should:
        #     TODO: Display a "game over" image, and
        #     TODO: "break" out of the game loop (to stop the program).
        #

        # TODO 5: See your Pong game for how to:
        #   TODO: Update the pygame display.
        pygame.display.update()


        #   NOTE:  Your screen will "lock up" until you have done the NEXT TODO.

# TODO 1: Call main.
main()

