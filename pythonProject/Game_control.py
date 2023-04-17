import Location
import Character
import random
import json


class GameControl:
    def __init__(self):
        self.rolls = 0
        self.MAX_ROLL = 3
        self.player = Character.User()
        self.location = Location.Location()
        # need instance variables for the player & location & timer (if needed)

# class Dice:
    def roll_die(self, amount, sides):
        rolls = []
        for i in range(amount):
            rolls.append(random.randint(1, sides))
        return rolls

    def assign_attributes(self, dice_values):
        self.player.change__init__(health=dice_values[0] + dice_values[1])
        self.player.change__init__(strength=dice_values[2] + dice_values[3])
        self.player.change__init__(speed=dice_values[4] + dice_values[5])

    def ask_roll_again(self):
        print("Roll for you attributes, your attributes consist of health, strength and speed:\nHealth is how many "
              "times you can get hit and keep fighting\nStrength is how hard you hit whoever you attack\nSpeed helps "
              "when you're dodging, attacking, or running away from enemies")
        print("Your current attributes are:\nHealth {} of 12 / Strength {} of 12 / Speed {} of 12"
              .format(self.player.health, self.player.health, self.player.speed))
        while self.rolls < self.MAX_ROLL:
            userinput = input("Would you like to roll for new attributes? (yes/no)\n")
            while userinput != ("yes" or " no"):
                userinput = input("Please enter a valid answer\nWould you like to roll for new attributes? (yes/no)")
            if userinput.lower() == "yes":
                new_rolls = self.roll_die(6, 6)
                self.assign_attributes(new_rolls)

                print('\nYour health is {} of 12, strength is {} of 12, speed is {} of 12'
                      .format(self.player.health, self.player.strength,
                              self.player.speed))
                self.rolls += 1
                print("You have rolled {}/3 times, you have {} rolls left".format(self.rolls, (3 - self.rolls)))
            else:
                break

    def ask_name(self):
        # print("Do you have a name?")
        name = input("Do you have a name?\n")
        self.player.change__init__(name=name)
        if name.lower() == "yes":
            # print("What is your name:")
            name = input("What is your name:\n")
            self.player.change__init__(name=name)
        elif name.lower() == "no":
            # print("What shall you be called:")
            name = input("What shall you be called:\n")
            self.player.change__init__(name=name)

    def make_blank_save(self):
        data = [{"blank_beginner_save": self.player.__dict__}]
        sf = json.dumps(data, indent=4, separators=(',', ': '))
        with open('JSON files/SavedCharacterData.json', "w") as outfile:
            outfile.write(sf)

    def save_data(self):
        save_name = input("Save name (Data will be saved under this name):\n")
        data = []
        with open('JSON files/SavedCharacterData.json') as outfile:
            data = json.load(outfile)
        print(data)
        for d in data:
            print("Beginning ran")
            print(data)
            print(d)
        for i in range(len(data)):
            if save_name == d:
                print("Save name found ran")
                save_replace = input("There is a previous save with this name, would you like to replace it? "
                                     "(yes/no)\n")
                while True:
                    if save_replace == "yes" or save_replace == "no":
                        break
                    else:
                        save_replace = input("Please input a valid response\n"
                                             "Would you like to replace the existing save?\n")
                if save_replace == "yes":
                    for key in d.keys:
                        if save_name == key:
                            key = self.player.__dict__
                            with open('JSON files/SavedCharacterData.json', 'w') as json_file:
                                json.dump(data, json_file,
                                          indent=4,
                                          separators=(',', ': '))
                else:
                    self.save_data()
            else:
                print("New save creation ran")
                data.append({
                    save_name: self.player.__dict__
                })
                with open('JSON files/SavedCharacterData.json', 'w') as json_file:
                    json.dump(data, json_file,
                              indent=4,
                              separators=(',', ': '))
                break

    # # with open('JSON files/SavedCharacterData.json', 'r') as f:
    # #     info = f.read()
    # #     info = info.replace(save_name, self.player.__dict__)
    # # with open('JSON files/SavedCharacterData.json', 'w') as f:
    # #     f.write(info)
    # # print("Save Updated")

    # def save_data(self):
    #     save_name = input("Save name (Data will be saved under this name):\n")
    #     data = {
    #         save_name: self.player.__dict__
    #     }
    #     sf = json.dumps(data, cls=FileEncoder)
    #     with open('JSON files/SavedCharacterData.json', "w") as outfile:
    #         outfile.write(sf)
    #     print('Data saved')

    def load_data(self):
        load_name = input("Save name (Data saved to this name will be loaded):\n")
        with open('JSON files/SavedCharacterData.json') as f:
            f = json.load(f)
        # for k in SavedCharacterData[load_name]:
        #     if k in self.player.attributes:
        #     self.player.attributes[k] = SavedCharacterData[load_name][k]
        for d in f:
            for key, value in d.items():
                if key == load_name:
                    for s in value:
                        # print(s)
                        v = "self." + s
                        if s in self.player.attributes.keys():
                            for a in value.values():
                                # print(a)
                                # print("True")
                                # print(v)
                                self.player.change__init__(v=a)
                                print(self.player.__dict__)
                                # print(v)
                                # print("{} loaded!".format(load_name))
                else:
                    print("Incorrect dictionary")
        # for i in f:
        #     for key in i.keys():
        #         if key == load_name:
        #             for i in f:
        #                 print(i)
        #                 for key in i.values():
        #                     print(key)
        #                     print(type(key))
        #                     for attributes in key.values():
        #                         print(attributes)
        #                         print(type(attributes))
        #                         for attribute_values in attributes.values():
        #                             if attribute_values in self.player.attributes:
        #                                 v = "self." + value
        #                                 self.player.change__init__(v=SavedCharacterData[load_name][value])
        #                                 print("{} loaded!".format(load_name))
        #                             else:
        #                                 print("Error loading attributes")
        #         else:
        #             print("Campaign save not found\nPlease input a valid Campaign name")
        #             self.load_data()

    def start_location(self):
        self.location.get_data()
        self.location.create_location_grid(3, 3)
        self.location.print_location_grid(self.location.grid)

    def run_location(self):
        self.location.player_movement()
        self.location.update_grid()
        self.location.create_location_grid(3, 3)
        self.location.print_location_grid(self.location.grid)

    def start_game(self):
        self.make_blank_save()
        print("Welcome to: \"GAME NAME\"\n", end='To start - ')
        load_ask = input("Do you have a previous saved campaign? (yes/no)\n")
        while True:
            if load_ask == "yes" or load_ask == "no":
                break
            else:
                load_ask = input("Please input a valid response\nDo you have a previous saved campaign? (yes/no)\n")
        if load_ask == "yes":
            gc.load_data()
        else:
            print("Please create a new save!")
            gc.save_data()
        print("Remember saves aren't automatic, if you want to save do it manually!")
        print("\n\n\n")

    def action_prompt(self):
        u = input("What would you like to do? (Options: move / look around / interact)")
        print(u)


gc = GameControl()
# #
gc.make_blank_save()
gc.save_data()
gc.save_data()
gc.save_data()
# gc.load_data()
# #
# gc.start_game()
# gc.ask_name()
# current_rolls = gc.roll_die(6, 6)
# gc.assign_attributes(current_rolls)
# gc.ask_roll_again()
# gc.start_location()
# while True:
#     gc.run_location()
