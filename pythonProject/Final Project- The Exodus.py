"""
    Project name: Final Project- The Exodus.py
    Description: A fully functional and extensive text based game
    Name: Samuel Rabinor
    Date: December/14/22
"""

import random
import logging
import os
import sys
import time
import datetime
import json


logging.basicConfig(level=logging.DEBUG, filename='debug-final.log')

class Character:
    def __init__(self):
        self.name = name
        self.health = 0
        self.strength = 0
        self.speed = 0
        self.magic = 0
        self.xp = 0
        self.is_alive = True
        self.MAX_HEALTH = 0
        logging.debug('Creating new Character object...')

    def set_dead(self):
        """
        Sets the is alive instance variable to false
        :return: nothing
        """
        self.is_alive = False

    def hit_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

    def dodge_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

class Location:
    def __init__(self):
        self.User_Input = input()

    def location(self):
        self.location_movement

    def forest_movement(self):
        print("You are in the forest. What would you like to do? "
              "(Options: explore/west/northwest/north/north-east/east/back)")

    def forest_west(self):
        print("You are in a clearing.")

    def forest_northwest(self):
        print("You find more forest, to the west, the forest seems to begin to thin out into a clearing perhaps?"
              "To the north you hear the muted sounds of a river or creek.")

    def forest_north(self):
        print("The sounds of the creek grow louder as the trees seem to grow taller, stronger and wider")

    def forest_north(self):
        print("Description needed.")

    def mountains(self):
        #self.mountain_description()
        self.mountains_movement()

    """
    def mountains_description(self):
        if ___:
            print("")
        elif ___:
            print("")
        elif ___:
            print("")
    """

    def graveyard(self):
        print("Description needed.")

class Time:
    def __init__(self):
        self.start_time = time.time()
        self.GAME_TIME_MULTIPLIER = 1

    def get_game_time(self):
        """
        Returns the current game time in seconds, adjusted based on the GAME_TIME_MULTIPLIER.
        """
        return (time.time() - self.start_time) * self.GAME_TIME_MULTIPLIER

    def set_timer(self, seconds):
        """
        Sets a timer for the specified number of seconds.
        """
        global current_time
        current_time = self.get_game_time()
        current_time += seconds

    """
    Get the current game time
    game_time = get_game_time()
    print("Current game time: {}".format(round(game_time)))

    Set a timer for x seconds
    x = input("Length of timer in seconds: ")
    set_timer(x)
    print("Timer set for {} seconds...".format(x))

    Wait for the timer to expire
    while get_game_time() < game_time + x:
    time.sleep(1)

    The timer has expired!
    print("Timer expired!")
    """

if __name__ == '__main__':
    pass