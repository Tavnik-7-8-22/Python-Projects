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


logging.basicConfig(level=logging.DEBUG, filename='debug-final.log')


class Character:
    """A class for holding information about Characters"""

    def __init__(self, name='unknown'):
        self.name = name                                    # Character name
        self.rolls = 0                                      # Rolls taken
        self.health = 0                                     # Character health
        self.strength = 0                                   # Character strength
        self.speed = 0                                      # Character speed
        self.XP = 0                                         # Character XP
        self.is_alive = True                                # Whether the Character is alive
        self.MAX_HEALTH = 60                                # Character max health
        self.MAX_ROLL = 3                                   # Max amount of rolls allowed
        self.weapon = False                                 # NNo character should carry weapon unless obtained
        logging.debug('Creating new Character object...')   # Debug statement

    def set_dead(self):
        """
        sets the is_alive instance variable to False
        :return: nothing
        """
        self.is_alive = False

    def show_health(self):
        """
        prints out the current health level of a Character
        :return: nothing
        """
        txt.print_slow("{}'s current health is {}.".format(self.name, self.health))

    def show_XP(self):
        """
                prints out the current XP level of a Character
                :return: nothing
                """
        txt.print_slow('{} current XP level is {}.'.format(self.name, self.XP))

    def roll_die(self):  # move out of character class
        """
        Rolls 6 dice to decide health, strength and speed.
        :return: the dice roll values
        """
        return [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    def assign_attributes(self, dice_values): #
        """
        Assigns values to attributes
        :param dice_values: The values to assign to the attribute
        :return: nothing
        """
        self.health = dice_values[0] + dice_values[1]
        self.strength = dice_values[2] + dice_values[3]
        self.speed = dice_values[4] + dice_values[5]

    def show_attributes(self):
        """
               prints out the current attributes of a Character
               :return: nothing
               """
        txt.print_slow("{}'s current health is {}, strength is {}, speed is {}.".format(self.name, self.health,
                                                                                        self.strength, self.speed))

    def ask_reroll(self):
        userInput = ""
        txt.print_slow("\n(The below attributes are your current health, strength and speed. You have 3 opportunities "
                       "to get new attributes.)\n")
        txt.print_slow('Your health is {} of 12, strength is {} of 12, speed is {} of 12.'.format(self.health, self.strength, self.speed))
        txt.print_slow("Is this correct, or are you misremembering?\nI only have so much patience so I recommend you "
                       "hurry.\nYou have three chances to remember them correctly if they are not already.\nDo you wish"
                       " to try and remember your attributes again? (Options: yes/no)\n")

        while self.rolls < self.MAX_ROLL:
            userInput = input()
            if userInput.lower() == "yes":
                new_rolls = self.roll_die()
                self.assign_attributes(new_rolls)
                txt.print_slow('\nYour health is {} of 12, strength is {} of 12, speed is {} of 12.'.format(self.health, self.strength, self.speed))
                self.rolls += 1
                if self.rolls == 1:
                    txt.print_slow("\nIs this correct or would you like to try and remember correctly this time? \nYou "
                                   "are trying my patience. You have tried once already. (Options: yes/no)\n")
                if self.rolls == 2:
                    txt.print_slow("This is twice you have tried now.\nIs this correct, or did you misremember once "
                                   "again?\nDo you need one more attempt. Remember correctly this time my patience "
                                   "wears thin. (Options: yes/no)\n")
                if self.rolls == 3:
                    txt.print_slow("My patience has been worn thin. This is thrice you have attempted now.\nIf these "
                                   "attributes remain incorrect then so be it. I tire of you quickly.\n")
                    time.sleep(1.5)
            elif userInput.lower() == "no":
                txt.print_slow("")
                break
            else:
                txt.print_slow("Please enter a valid answer. (Options: yes/no)\n")
                logging.debug('Invalid answer in ask_reroll')  # Debug statement

    def hit_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

    def dodge_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

    def attack(self, victim):  # Imp is not the only enemy I will be coding there are 4 more (one in graveyard,
        # deep forest, mountain, high mountain)
        """
        attack option for Characters
        :param victim: the victim of the attack
        :return: nothing
        """
        crit_hit = random.randint(6, 8)
        strong_hit = random.randint(4, 6)
        even_hit = random.randint(3, 5)
        weak_hit = random.randint(2, 4)
        txt.print_slow('The {} attempts to attack you.'.format(self.name))  # This is the code used by all enemies and
        # it is overridden in the user class so all enemies attack "you"
        if self.hit_chance() > victim.dodge_chance():
            if random.randint(0, 100) >= 51:
                victim.health -= crit_hit
                txt.print_slow("The {} lands a critical hit against you.".format(self.name))
            elif victim.strength < self.strength:
                victim.health -= strong_hit
                txt.print_slow("The {} lands a powerful blow against you.".format(self.name))
            elif victim.strength == self.strength:
                victim.health -= even_hit
                txt.print_slow("Though your strength is equally matched, the {} manages to strike you.".format(self.name))
            elif victim.strength > self.strength:
                victim.health -= weak_hit
                txt.print_slow("You are far stronger than the {}, though the {} leaps and strikes, you easily blocks "
                               "the {}'s attack.".format(self.name, self.name, self.name))
        else:
            txt.print_slow("You attempt to dodge but the {} manages to strike you.".format(self.name))
            victim.health -= weak_hit
        victim.show_health()
        if victim.health <= 0:
            self.XP += victim.XP
            victim.XP = 0
            victim.set_dead()

    def feed_food(self):
        """
        feed/heal option for Character
        :return: nothing
        """
        self.health += random.randint(0, 3)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        txt.print_slow('{} ate food.'.format(self.name))
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."  # assertion statement

    def feed_nut_food(self):
        self.health += random.randint(3, 6)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        txt.print_slow('{} ate nutritious food.'.format(self.name))
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."  # assertion statement


class User(Character):
    def __int__(self, name='unknown'):
        super().__init__()
        self.is_alive = True

    def show_health(self):  # This is repeated so I can change the text printed when called (Your instead of {})
        """
        prints out the current health level of a User
        :return: nothing
        """
        txt.print_slow('Your current health is {}.'.format(self.health))

    def show_XP(self):  # This is repeated so I can change the text printed when called (Your instead of {})
        """
        prints out the current XP level of a User
        :return: nothing
        """
        txt.print_slow('Your current XP level is {}.'.format(self.XP))

    def attack(self, victim):
        """
        attack option for User
        :param victim: the victim of the attack
        :return: nothing
        """
        if self.weapon:
            crit_hit = random.randint(6, 8) * 2
            strong_hit = random.randint(4, 6) * 2
            even_hit = random.randint(3, 5) * 2
            weak_hit = random.randint(2, 4) * 2
        else:
            crit_hit = random.randint(6, 8)
            strong_hit = random.randint(4, 6)
            even_hit = random.randint(3, 5)
            weak_hit = random.randint(2, 4)
        txt.print_slow('\nYou attempt to attack {}.'.format(victim.name))
        if self.hit_chance() > victim.dodge_chance():
            if random.randint(0, 100) >= 51:
                victim.health -= crit_hit
                txt.print_slow("You land a critical hit against the {}.".format(victim))
            elif victim.strength < self.strength:
                victim.health -= strong_hit
                txt.print_slow("You land a powerful blow against {}.".format(victim.name))
            elif victim.strength == self.strength:
                victim.health -= even_hit
                txt.print_slow("Though your strength is equally matched, you manage to strike {}.".format(victim.name))
            elif victim.strength > self.strength:
                victim.health -= weak_hit
                txt.print_slow("{} is far stronger than you, though you leap and strikes, {} easily blocks your attack.".format(
                    victim.name, victim.name))
        else:
            txt.print_slow("The {} dodges your attack.".format(victim.name))
        if victim.health <= 0:
            self.XP += victim.XP
            victim.XP = 0
            victim.set_dead()

    def feed_food(self):  # This is repeated so I can change the text printed when called (You eat instead of {} ate)
        """
        feed/heal option for User
        :return: nothing
        """
        self.health += random.randint(0, 3)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        txt.print_slow('You eat food.')
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."  # assertion statement

    def feed_nut_food(self):  # This is repeated so I can change the text printed when called (You eat instead of {} ate)
        self.health += random.randint(3, 6)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        txt.print_slow('You eat nutritious food.')
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."  # assertion statement

    def show_attributes(self):   # This is repeated so I can change the text printed when called (Your instead of {})
        """
        prints out the current attributes of a Character
        :return: nothing
        """
        txt.print_slow('Your current health is {}, strength is {}, speed is {}.'.format(self.health, self.strength, self.speed))


class Enemy(Character):
    def __init__(self, name='unknown'):
        super().__init__()
        self.name = name  # Code would randomly break if i didn't have this in it for some reason
        self.is_alive = True


class Imp(Enemy):
    def __init__(self, name='unknown'):
        super().__init__()
        self.name = name  # Code would randomly break if i didn't have this in it for some reason
        self.speed = random.randint(1, 6) + random.randint(1, 6) + 5


class TextDelays:
    def print_slow_glitch(self, str):
        txt.print_slow("\nYou step forth into the world of Exodus. After walking for a while, you realize your "
                          "surroundings are all blurred and shaky, as if censored by something")
        txt.dramatic_pause("...")

    def print_slow(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.02)

    def print_slower(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.3)

    def print_slowest(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.5)

    def dramatic_pause(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(1.75)

class Spell:
    def decipher(self, text):
        """
        Will encipher a string
        :param text: the string you are deciphering
        :return: the deciphered string
        """
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shifted_upper = upper[22:] + upper[:22]
        lower = "abcdefghijklmnopqrstuvwxyz"
        shifted_lower = lower[22:] + lower[:22]
        encipher_str = ""

        for ch in text:
            if ch in upper:
                ch_pos = upper.index(ch)
                encipher_str += shifted_upper[ch_pos]
            elif ch in lower:
                ch_pos = lower.index(ch)
                encipher_str += shifted_lower[ch_pos]
            else:
                encipher_str += ch
        return encipher_str

class Game:
    def __init__(self):
        self.gardenDiscovered = False
        self.encounter = 0
        self.glitch = True

    def clear(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def dev_testing_space(self):
        game.clear()
        txt.print_slow("Welcome to the dev space, if you are not a developer or game tester please return to the game.\n"
              "Test: (introScene / campsite / impAttack / showGarden / showForest)\n"
              "currently unavailable (showDeeperForest / showMountain / Graveyard)\n")
        userInput = input()
        if userInput == "introScene":
            game.introScene()
        elif userInput == "campsite":
            game.Campsite()
        elif userInput == "impAttack":
            game.impAttack()
        elif userInput == "showGarden":
            game.showGarden()
        elif userInput == "showForest":
            game.showForest()
        elif userInput == "showDeeperForest":
            game.showDeeperForest
        elif userInput == "showMountain":
            game.showMountain
        elif userInput == "showGraveyard":
            game.Graveyard

    def game_end(self):
        time.sleep(2)
        game.clear()
        txt.print_slower("This is not how your story goes.    \n")
        txt.print_slower("Your memories are too far gone.")
        txt.dramatic_pause(" ")
        txt.print_slower("We must try again.   \n")
        txt.print_slower("I have no use of you any longer.   \n")
        txt.print_slowest("Fade... forget... and be forgotten.   \n")
        txt.print_slower("We shall try once again")
        txt.dramatic_pause(" ... ")
        txt.print_slowest(" soon.   ")
        time.sleep(10)
        sys.exit()

    def levelUP(self):
        txt.print_slow("")
        #if character

    def introScene(self):
        directions = ["left", "right", "forward"]
        txt.print_slow("You find yourself at a campsite, you are familiar with this place, and yet you dont know why.\nThis is "
              "the beginning, your journey begins here, where shall you go next? (Options: left/right/forward)\n")
        userInput = ""
        while userInput not in directions:
            txt.print_slow("Where shall you journey:\n")
            userInput = input()
            try:
                if userInput.lower() == "devtestspace":
                    game.dev_testing_space()
                elif userInput.lower() == "left":
                    print()
                    print("\n(This is supposed to happen. Wait until prompted to type.)")
                    txt.print_slow("\nXli iriqc csy wiio mw xli revvexsv lmqwipj, li wxerhrw filmrh csy orsa erh wtieow"
                        " pmiw mrxs csyv iev.\nXs hijiex lmq, csy qywx hmk yt e kvezi jvsq csyv tewx. Xli "
                        "reqi psrk gsvvytxih fc xli revvexsvw xamwxih xsrkyi.\nXlivi csy ampp jmrh xli "
                        "aietsr csy wiio, zirxyvi jvsq csyv irgeqtqirx fyx fi wyvi rsx xs liih lmw xvmgoivc."
                        "\nXs jmrh lmq erh ffvmrk nywxmgi, csy qywx xvezip FEGOAEVHW. Xlivi csy ampp jmrh "
                        "lmq, mj csy hijiex lmq, csy ampp jmreppc fi jviih.\n")
                    game.clear()
                    game.Campsite()
                elif userInput.lower() == "right":
                    print()
                    txt.print_slow("\n(This is supposed to happen. Wait until prompted to type.)"
                        "\nXli iriqc csy wiio mw xli revvexsv lmqwipj, li wxerhrw filmrh csy orsa erh wtieow "
                        "pmiw mrxs csyv iev.\nXs hijiex lmq, csy qywx hmk yt e kvezi jvsq csyv tewx. Xli "
                        "reqi psrk gsvvytxih fc xli revvexsvw xamwxih xsrkyi.\nXlivi csy ampp jmrh xli "
                        "aietsr csy wiio, zirxyvi jvsq csyv irgeqtqirx fyx fi wyvi rsx xs liih lmw xvmgoivc."
                        "\nXs jmrh lmq erh ffvmrk nywxmgi, csy qywx xvezip FEGOAEVHW. Xlivi csy ampp jmrh "
                        "lmq, mj csy hijiex lmq, csy ampp jmreppc fi jviih.\n")
                    game.clear()
                    game.Campsite()
                elif userInput.lower() == "forward":
                    print()
                    txt.print_slow("\n(This is supposed to happen. Wait until prompted to type.)"
                                    "\nXli iriqc csy wiio mw xli revvexsv lmqwipj, li wxerhrw filmrh csy orsa erh wtieow "
                                   "pmiw mrxs csyv iev.\nXs hijiex lmq, csy qywx hmk yt e kvezi jvsq csyv tewx. Xli "
                                   "reqi psrk gsvvytxih fc xli revvexsvw xamwxih xsrkyi.\nXlivi csy ampp jmrh xli "
                                   "aietsr csy wiio, zirxyvi jvsq csyv irgeqtqirx fyx fi wyvi rsx xs liih lmw xvmgoivc."
                                   "\nXs jmrh lmq erh ffvmrk nywxmgi, csy qywx xvezip FEGOAEVHW. Xlivi csy ampp jmrh "
                                   "lmq, mj csy hijiex lmq, csy ampp jmreppc fi jviih.\n")
                    game.clear()
                    game.Campsite()
                elif userInput.lower() == "backwards":
                    txt.print_slow("\nIt seems like you can't do anything right, can you? As you stare out into the ruins of your home, memories"
                          " flash back to you, a happy family, a strange shadow, a stranger man, a splitting scream, your"
                          " family's broken bodies at your feet,\nthe strange man rising from the ground behind you, his"
                          " voice in your ear, familiar words... Welcome, traveler, to Exodus. The strange man rises "
                          " before you and you hear yourself scream as the world goes black around you.")
                    game.game_end()
                else:
                    txt.print_slow("\nError.. Invalid answer. Please input left, right, or forward.")
            finally:
                print()

    def Campsite(self):
        directions = ['left', 'right', 'forward', 'garden']
        if self.glitch:
            txt.print_slow("That's strange, wasn't I just here a moment ago? ... Must be Deja Vu I guess.")
            self.glitch = False
        if self.encounter == 1 and not self.gardenDiscovered == True:
            self.gardenDiscovered = True
            txt.print_slow("\nYou notice a small garden that you hadn't seen before, you could probably explore it and find food to heal yourself.\n"
                  "New option discovered: garden. (Options: left/forward/right/garden)\n")
        elif not self.gardenDiscovered:
            txt.print_slow("\nYou look around at your campsite, it is familiar, but it is not comforting, and you still dont know why or "
                  "how you know this strange place. (Options: left/forward/right)\n")
        else:
            txt.print_slow("\nYou look around at your campsite, it is familiar, but it is not comforting, and you still dont know why or "
                  "how you know this strange place, you now notice the garden as well. (Options: left/forward/right/garden)\n")
        userInput = ""
        while userInput not in directions:
            userInput = input()
            if userInput.lower() == "devtestspace":
                game.dev_testing_space()
            elif userInput.lower() == "left":
                game.showForest()
            elif userInput.lower() == "right":
                game.showMountains()
            elif userInput.lower() == "forward":
                game.howGraveyard()
            elif userInput.lower() == "backwards":
                game.bossfight()
            elif userInput.lower() == "garden":
                game.showGarden()
            else:
                txt.print_slow("Please enter a valid option.")


    def impAttack(self):
        self.encounter += 1
        imp = Imp('Imp')
        current_enemy_roll = imp.roll_die()
        imp.assign_attributes(current_enemy_roll)
        imp.show_attributes()
        user.show_attributes()
        if not imp.is_alive:
            game.showForest()
        else:
            while user.is_alive:
                txt.print_slow("\nWhat will you do? (Options: fight/flee/wait)\n")
                userInput = input()
                if userInput == "fight":
                    user.attack(imp)
                    if imp.is_alive:
                        if imp.health // 2 == 1:
                            if random.randint(0, 10) >= 7:
                                imp.feed_nut_food()
                            else:
                                imp.feed_food()
                        imp.attack(user)
                        if not user.is_alive:
                            game.game_end()
                    else:
                        game.showForest()
                        imp.is_alive = True
                elif userInput == "flee":
                    if user.speed > imp.speed:
                        game.Campsite()
                    else:
                        txt.print_slow("\nYou attempt to flee, however the imp catches up to you.")
                        imp.attack(user)
                        if not user.is_alive:
                            game.game_end()
                elif userInput == "wait":
                    imp.attack(user)
                    if not user.is_alive:
                        game.game_end()
                    else:
                        txt.print_slow("\nWhy are you waiting in the middle of battle? Do something!")

    def showGarden(self):
        global food
        global nut_food
        txt.print_slow("You stroll though the garden until you find something that looks fresh.")
        if random.randint(0, 100) < 80:
            food += 1
            nut_food += 1

    def showForest(self):
        global food
        global nut_food
        directions = ["deeper", "explore", "leave"]
        txt.print_slow("\nThe forest is shady and yet, eerily quiet all of the woodland creatures you would normally expect to "
              "find in a forest are gone.")
        if random.randint(0, 100) <= 50:
            txt.print_slow("From the bushes comes a growl and suddenly an imp runs out from the bushes "
                  "and attacks you. Stunned for a moment, you quickly prepare for battle.\n Before you attack a memory"
                  "flashes by, you cant decipher much but it helps remind you that goblins are exceedingly fast.")
            game.impAttack()
        else:
            userInput = ""
            while userInput not in directions:
                txt.print_slow("Where would you like to go? (Options: deeper/explore/leave)")
                userInput = input()
                chance = random.randint(0, 100)
                if userInput.lower() == "deeper":
                   game.showDeeperForest()
                elif userInput.lower() == "explore":
                    if chance < 5:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You find a mysterious scroll,\nIt reads, there is a code in the text above, there is "
                              "a spell hidden in the mountain tops. if you find both of these, it is possible to obtain a "
                              "weapon, one powerful enough to help you defeat your enemy. If you want to regain "
                              "your memory, you must go backwards.\nSomething tells you that is the most info you will find"
                              "in the forest.")
                        game.showForest()
                    elif chance < 15:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You find a mysterious scroll,\nIt reads, there is a code in the text above, there is a "
                              "spell hidden in this world. These items will help you on your journey. Beware the enemy at "
                              "your back, he is closer than you think.\nMaybe if you keep exploring you'll find more clues,"
                              "for now, it seems like you have to search for a spell of some kind.")
                        game.showForest()
                    elif chance < 35:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You find a scroll with illegible text, you manage to understand some of it, all you can "
                              "comprehend though is mountain top, spell and something about a code.\nMaybe if you keep "
                              "exploring you'll find more clues.")
                        game.showForest()
                    elif chance < 65:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You find a stick, you swing it around and use it as a walking stick for a while but before "
                              "long it breaks so you throw it back into the bushes.")
                        game.showForest()
                    elif chance < 85:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You find some food!")
                        food += 1
                        game.showForest()
                    elif chance <= 100:
                        txt.print_slow("You search the forest, looking for something useful.")
                        txt.print_slow("You found some extra nutritious food!")
                        nut_food += 1
                        game.showForest()
                elif userInput.lower() == "leave":
                    game.Campsite()
                else:
                    txt.print_slow("Please enter a valid option.")

if __name__ == "__main__":
    txt = TextDelays()
    game = Game()
    while True:
        txt.print_slow("DISCLAIMER: IF AT ANY POINT THROUGHOUT THE GAME IT SEEMS TO FREEZE OR YOU ARE NOT PROMPTED TO "
                       "TYPE ANYTHING, DO NOT TYPE. THIS IS INTENTIONAL, SIMPLY WAIT AND THE PROGRAM WILL CONTINUE.")
        time.sleep(4)
        game.clear()
        txt.print_slow("Welcome, traveler, to Exodus. In this world, you must rely on three attributes. Health, strength and speed.\n"
              "Health represents how many times you can be hit before you die. Strength represents how hard you hit your enemies.\nSpeed "
              "represents whether you will be able to hit and/or flee from your enemies.I am sure you are confused as "
              "to why you are here, and how you got here.\nWhy dont we start at the beginning. Do you remember your name, explorer of Exodus:\n")
        name = input()
        if name.lower() == "yes":
            txt.print_slow("What is your name:\n")
            name = input()
        elif name.lower() == "no":
            txt.print_slow("\nUnfortunate, we must give you one then. What shall you be called:\n")
            name = input()
        txt.print_slow("\nVery well {}, next you must recall your attributes.".format(name))
        user = User(name)
        current_rolls = user.roll_die()
        user.assign_attributes(current_rolls)
        user.ask_reroll()
        time.sleep(2)
        game.clear()

        txt.print_slow("Let us begin from the first moments of your great journey...")
        game.introScene()
