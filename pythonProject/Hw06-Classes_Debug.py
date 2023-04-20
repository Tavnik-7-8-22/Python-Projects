"""
    Project name: Hw06-Classes_Debug.py
    Description: Debugging for a text based game where a Hero battles an Orc
    Name: Samuel Rabinor
    Date: November/28/2022
"""

import random
import logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log')


class Sprite:
    """A class for holding information about Sprites"""

    def __init__(self, name='unknown'):
        self.name = name            # sprite name
        self.x = 0                  # position on screens X-axis
        self.y = 0                  # position on screens Y-axis
        # self.health = 10          # sprite health
        self.health = 30
        # Prediction - There will be several more rounds as both sprite objects start with more health and greater max health
        # Result - Rounds increased not as much as they thought they would but rather from a range of 1-4 to a range of 3-7
        self.strength = 15          # sprite strength
        self.loot = 50              # sprite loot
        self.is_alive = True        # whether the sprite is alive
        # self.MAX_HEALTH = 15      # sprites max health
        self.MAX_HEALTH = 50
        # Prediction - Nothing will change because sprite objects still start with the same health as before
        # Result - I was correct, nothing much changed in the simulations
        self.magic_key = False      # whether the sprite has a magic key
        logging.debug('Creating new sprite object...')  # Debug statement

    def set_dead(self):
        """
        sets the is_alive instance variable to False
        :return: nothing
        """
        self.is_alive = False

    def show_health(self):
        """
        prints out the current health level of a sprite
        :return: nothing
        """
        print('{} current health is {}.'.format(self.name, self.health))

    def show_loot(self):
        """
        prints out the current loot level of a sprite
        :return: nothing
        """
        print('{} has total loot of {}.'.format(self.name, self.loot))

    def attack(self, victim):
        """
        prints out sprite attacking another sprite
        :param victim: the victim of the attack
        :return: nothing
        """
        print('{} attacks {}.'.format(self.name, victim.name))
        if victim.strength < self.strength:
            victim.health -= random.randint(0, 15)
        else:
            victim.health -= random.randint(0, 5)
        victim.show_health()
        if victim.health <= 0:
            self.loot += victim.loot
            victim.loot = 0
            victim.set_dead()
            if victim.magic_key:
                victim.magic_key = False
                self.magic_key = True
                print("{} received the magic key!".format(self.name))

    def feed(self):
        """
        prints out sprite feeding to heal
        :return: nothing
        """
        self.health += random.randint(0, 3)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        print('{} ate food.'.format(self.name))
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."  # assertion statement

    def move(self):
        """
        moves sprite by up to 1 position
        :return: nothing
        """
        assert self.health >= 0, "{} cannot move, {} is dead!".format(self.name, self.name)  # assertion statement
        print("{} is currently at ({}, {})".format(self.name, self.x, self.y))
        if self.health < 3:
            print("{} is too low health to move.".format(self.name))
        else:
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)
            print("{} moves to ({}, {})".format(self.name, self.x, self.y))

    def __repr__(self):
        """
        returns the name, health, strength, and position of the sprite
        :return: nothing
        """
        return "{} health is {}, strength is {}, position is ({}, {})".format(self.name, self.health, self.strength,
                                                                              self.x, self.y)


"""
test_sprite = Sprite('Test_Sprite')
test_sprite2 = Sprite('Test_Sprite2')
test_sprite.attack(test_sprite2)
test_sprite.feed()
test_sprite.show_loot()
"""


class Enemy(Sprite):
    """A class for holding information about enemies"""

    def __init__(self, name='unknown'):
        super().__init__()
        self.name = name
        self.loot = random.randint(0, 20)
        self.strength = random.randint(1, 15)
        if random.randint(0, 100) >= 75:
            self.magic_key = True
        logging.debug('Created enemy with name of {}'.format(self.name))  # Debug statement

    def set_dead(self):
        """
        sets the is_alive instance variable to False
        :return: nothing
        """
        self.is_alive = False
        print("{} dies: My evil comrades will avenge my death!".format(self.name))


"""
test_enemy = Enemy('Test_Enemy')
test_enemy.show_health()
test_enemy.show_loot()
test_enemy.set_dead()
"""


class Avatar(Sprite):
    """A class for holding information about the Avatar"""

    def __init__(self, name='unknown'):
        super().__init__()
        self.name = name
        self.loot = 0
        self.strength = random.randint(1, 10)
        logging.debug('Created avatar with name of {}'.format(self.name))  # Debug statement

    def set_dead(self):
        """
        sets the is_alive instance variable to False
        :return: nothing
        """
        self.is_alive = False
        print("{} dies: Alas! All is lost.".format(self.name))


"""
test_avatar = Avatar('Test_Avatar')
test_avatar.show_health()
test_avatar.show_loot()
test_avatar.set_dead()
"""

if __name__ == '__main__':
    orc = Enemy('Orc')
    hero = Avatar('Hero')
    print(orc)  # accessing repr function
    print(hero)  # accessing repr function
    Round = 0
    # Following text runs until one sprite dies
    while True:
        Round += 1
        print("\nRound: {}".format(Round))
        hero.attack(orc)
        if orc.is_alive:
            orc.feed()
            orc.move()
        else:
            break
        orc.attack(hero)
        if hero.is_alive:
            hero.feed()
            hero.move()
        else:
            break
