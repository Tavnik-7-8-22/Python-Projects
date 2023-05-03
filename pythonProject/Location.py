import json
import random
import Colors
import logging
logging.basicConfig(level=logging.DEBUG, filename='Location-debug.log')


class Location:
    def __init__(self):
        self.player = "[" + Colors.BLUE + "P" + Colors.END + "]"
        self.empty_space = "[ ]"
        self.enemy = "[" + Colors.RED + "E" + Colors.END + "]"
        self.tree = "[" + Colors.GREEN + "T" + Colors.END + "]"
        self.location_edge = Colors.GREYBG + "[#]" + Colors.END
        self.grid = []
        self.location_data = ""
        self.ZO_location = "Forest"
        self.move_count = 5
        self.visibility = 5
        self.update_temp_var = self.empty_space
        self.entrance = "[" + Colors.WHITE + "E" + Colors.END + "]"
        self.moves_UPDOWN = 0
        self.moves_UPDOWN_approach = 3
        self.moves_RIGHTLEFT = 0
        self.moves_RIGHTLEFT_approach = 3
        self.curr_pos = [self.moves_RIGHTLEFT, self.moves_UPDOWN]
        self.boarder_distance = 0
        self.campaign_name = ''
        self.distance_to_boarder_UPOWN = self.boarder_distance
        self.distance_to_boarder_RIGHTLEFT = self.boarder_distance
        self.approach_grid_movement = False
        logging.debug('__init__ accessed')

    def assign_campaign_name(self, var, val):
        logging.debug('Assigned campaign name')
        logging.debug('Called from Game_control')
        setattr(self, var, val)

    def set_location(self):
        logging.debug('Set location to middle of graph')
        logging.debug('Called from self.player_movement()')
        self.grid[len(self.grid)//2][len(self.grid)//2] = self.player

    # def set_boarder_location(self):
    #     logging.debug(f'Setting [P] <player> to coordinates ({self.moves_RIGHTLEFT_approach}, '
    #                   f'{self.moves_UPDOWN_approach})')
    #     self.grid[self.moves_RIGHTLEFT_approach][self.moves_UPDOWN_approach] = self.player

    def check_location(self):
        logging.debug('Unfinished function')
        return self.ZO_location

    def change_location(self, new_location):
        logging.debug('Unfinished function')
        pass

    def get_data(self):
        logging.debug('Taking data for Location descriptions and assigning it to self.location_data')
        logging.debug('Called at the beginning of Location run')
        f = open('JSON files/Location_info.json')
        location_info_raw = f.read()
        location_info = json.loads(location_info_raw)
        self.location_data = location_info

    def create_location_grid(self, w, h):
        logging.debug('Creating a grid with specified w <width> and h <height>')
        logging.debug('Called at the beginning of Location run')
        self.grid = []
        for i in range(w):
            row = []
            for j in range(h):
                row.append(self.empty_space)
            self.grid.append(row)
        self.randomize_grid()

    def print_location_grid(self):
        logging.debug('Printing out the grid')
        logging.debug('Called at the beginning of Location run and end of every loop')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=' ')
            print()

    def increase_visibility(self):
        logging.debug('Increasing visibility by 2 grid spaces')
        self.visibility += 2

    def decrease_visibility(self):
        logging.debug('Decreasing visibility by 2 grid spaces')
        self.visibility -= 2

    def randomize_grid(self):
        logging.debug('Randomizes the grid after creation')
        logging.debug('Called at the beginning of Location run')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                random_gen = random.randint(0, 100)
                if random_gen <= 1:
                    random_gen = self.enemy
                elif random_gen <= 8:
                    random_gen = self.tree
                elif random_gen <= 100:
                    random_gen = self.empty_space
                self.grid[i][j] = random_gen

    def randomize_grid_north(self):
        logging.debug('Randomizes first row of grid')
        logging.debug('Called after every northward movement call')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if i == 0:
                    random_gen = random.randint(0, 100)
                    if random_gen <= 1:
                        random_gen = self.enemy
                    elif random_gen <= 8:
                        random_gen = self.tree
                    elif random_gen <= 100:
                        random_gen = self.empty_space
                    elif random_gen == 0:
                        random_gen = self.entrance
                    self.grid[i][j] = random_gen

    def randomize_grid_west(self):
        logging.debug('Randomizes first column of grid')
        logging.debug('Called after every westward movement')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if j == 0:
                    random_gen = random.randint(0, 100)
                    if random_gen <= 1:
                        random_gen = self.enemy
                    elif random_gen <= 8:
                        random_gen = self.tree
                    elif random_gen <= 100:
                        random_gen = self.empty_space
                    self.grid[i][j] = random_gen

    def randomize_grid_south(self):
        logging.debug('Randomizes last row of grid')
        logging.debug('Called after every southern movement')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if i == len(self.grid) - 1:
                    random_gen = random.randint(0, 100)
                    if random_gen <= 1:
                        random_gen = self.enemy
                    elif random_gen <= 8:
                        random_gen = self.tree
                    elif random_gen <= 100:
                        random_gen = self.empty_space
                    self.grid[i][j] = random_gen

    def randomize_grid_east(self):
        logging.debug('Randomizes last column of grid')
        logging.debug('Called after every eastward movement')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if j == len(self.grid) - 1:
                    random_gen = random.randint(0, 100)
                    if random_gen <= 1:
                        random_gen = self.enemy
                    elif random_gen <= 8:
                        random_gen = self.tree
                    elif random_gen <= 100:
                        random_gen = self.empty_space
                    self.grid[i][j] = random_gen

    def update_grid_north(self):
        logging.debug('Moves entire grid content down one grid space excluding last row and updating '
                      'self.update_temp_var')
        logging.debug('Called after every northward movement call')
        for i in reversed(range(len(self.grid))):
            for j in reversed(range(len(self.grid[i]))):
                # print(temp_var)
                if i != 0:
                    if self.grid[i-1][j] == self.player:
                        self.grid[(len(self.grid)//2)+1][len(self.grid)//2] = self.update_temp_var
                        # # print(self.update_temp_var)
                        # # print("Changed to temp var")
                        # if self.update_temp_var == self.enemy:
                        #     self.trigger_event
                    elif self.grid[i][j] == self.player:
                        self.update_temp_var = self.grid[(len(self.grid) // 2) - 1][len(self.grid) // 2]
                        # # print(self.update_temp_var)
                        # # print("Assigned temp var")
                    else:
                        self.grid[i][j] = self.grid[i-1][j]

    def update_grid_west(self):
        logging.debug('Moves entire grid content to the left one grid space excluding last row and updating '
                      'self.update_temp_var')
        logging.debug('Called after every westward movement')
        for i in reversed(range(len(self.grid))):
            for j in reversed(range(len(self.grid[i]))):
                # print(temp_var)
                if j != 0:
                    if self.grid[i][j-1] == self.player:
                        self.grid[len(self.grid)//2][(len(self.grid)//2)+1] = self.update_temp_var
                        # # print(self.update_temp_var)
                        # # print("Changed to temp var")
                        # if self.update_temp_var == self.enemy:
                        #     self.trigger_event
                    elif self.grid[i][j] == self.player:
                        self.update_temp_var = self.grid[(len(self.grid))//2][(len(self.grid)//2)-1]
                        # # print(self.update_temp_var)
                        # # print("Assigned temp var")
                    else:
                        self.grid[i][j] = self.grid[i][j-1]

    def update_grid_south(self):
        logging.debug('Moves entire grid content up one grid space excluding first row and updating '
                      'self.update_temp_var')
        logging.debug('Called after every southern movement')
        # # print(f"{(len(self.grid)//2)+1,(len(self.grid))//2}")
        # # print(f"{self.grid[(len(self.grid)//2)+1][(len(self.grid))//2]}")
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # # print(f"{i, j}")
                if i != len(self.grid)-1:
                    if self.grid[i+1][j] == self.player:
                        self.grid[(len(self.grid)//2)-1][len(self.grid)//2] = self.update_temp_var
                        # # print(self.update_temp_var)
                        # # print("Changed to temp var")
                        # if self.update_temp_var == self.enemy:
                        #     self.trigger_event
                    elif self.grid[i][j] == self.player:
                        self.update_temp_var = self.grid[(len(self.grid)//2)+1][(len(self.grid))//2]
                        # # print(self.update_temp_var)
                        # # print("Assigned temp var")
                    else:
                        self.grid[i][j] = self.grid[i+1][j]

    def update_grid_east(self):
        logging.debug('Moves entire grid content to the right one grid space excluding last row and updating '
                      'self.update_temp_var')
        logging.debug('Called after every eastward movement')
        # # print(f"{(len(self.grid)//2)+1,(len(self.grid))//2}")
        # # print(f"{self.grid[(len(self.grid)//2)+1][(len(self.grid))//2]}")
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # # print(f"{i, j}")
                # # print(temp_var)
                if j != len(self.grid)-1:
                    if self.grid[i][j+1] == self.player:
                        self.grid[len(self.grid)//2][(len(self.grid)//2)-1] = self.update_temp_var
                        # # print(self.update_temp_var)
                        # # print("Changed to temp var")
                        # if self.update_temp_var == self.enemy:
                        #     self.trigger_event
                    elif self.grid[i][j] == self.player:
                        self.update_temp_var = self.grid[len(self.grid)//2][((len(self.grid))//2)+1]
                        # # print(self.update_temp_var)
                        # # print("Assigned temp var")
                    else:
                        self.grid[i][j] = self.grid[i][j+1]

    def location_boarders(self, boarder_distance):
        logging.debug('Assigns border distance, assigns it to self.boarder distance, and creates boarders where needed')
        logging.debug('Called in Location loop after self.revert_grid')
        self.boarder_distance = boarder_distance
        self.distance_to_boarder_UPOWN = (boarder_distance - abs(self.moves_UPDOWN))
        self.distance_to_boarder_RIGHTLEFT = (boarder_distance - abs(self.moves_RIGHTLEFT))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.moves_UPDOWN < 0 or self.moves_RIGHTLEFT < 0:
                    if -abs(self.distance_to_boarder_UPOWN) > -abs(self.visibility//2):
                        self.grid[len(self.grid)-1][j] = self.location_edge
                        logging.debug('Changed last grid down of grid')
                        # print(self.moves_UPDOWN)
                        # print("Reached location edge (south)")
                    elif -abs(self.distance_to_boarder_RIGHTLEFT) > -abs(self.visibility//2):
                        self.grid[i][0] = self.location_edge
                        logging.debug('Changed last row left of grid')
                        # print(self.moves_RIGHTLEFT)
                        # print("Reached location edge (east)")
                elif self.moves_UPDOWN > 0 or self.moves_RIGHTLEFT > 0:
                    if self.distance_to_boarder_UPOWN < (self.visibility//2):
                        print("changed grid")
                        self.grid[0][j] = self.location_edge
                        logging.debug('Changed first row up of grid')
                        # print(self.moves_UPDOWN)
                        # print("Reached location edge (north)")
                    elif self.distance_to_boarder_RIGHTLEFT < (self.visibility//2):
                        self.grid[i][len(self.grid)-1] = self.location_edge
                        logging.debug('Changed first row right of grid')
                        # print(self.moves_RIGHTLEFT)
                        # print("Reached location edge (west)")

    def check_empty_file(self):
        logging.debug('Checks file for characters, if the file is empty it creates a new save, otherwise it runs '
                      'self.save_grid')
        logging.debug('Called only for the purpose of clearing SavedGridData.json')
        with open("JSON files/SavedGridData.json", 'r') as f:
            one_char = f.read(1)
            if not one_char:
                data = [
                    {self.campaign_name: {"("
                                          "" + str(self.moves_RIGHTLEFT) + ","
                                                                           "" + str(self.moves_UPDOWN) + ")"
                                                                                                         "": self.grid}}
                    ]
                sf = json.dumps(data, indent=4, separators=(',', ': '))
                with open('JSON files/SavedGridData.json', "w") as outfile:
                    outfile.write(sf)
                print("Created save 0")
            else:
                print("Passed grid save")
                self.save_grid()

    def save_grid(self):
        logging.debug('Saves grid under campaign name and coordinates if grid is saved loads saved grid')
        logging.debug('Called in Location loop')
        grid_name = "(" + str(self.moves_RIGHTLEFT) + "," + str(self.moves_UPDOWN) + ")"
        with open('JSON files/SavedGridData.json') as outfile:
            data = json.load(outfile)
            times_checked = len(data)
            times_run = 1
        for d in data:
            for key, value in d.items():
                for k, v in value.items():
                    if key == self.campaign_name:
                        # print(f"k:{k}, grid_name:{grid_name}")
                        if k == grid_name:
                            self.grid = v
                            print("grid loaded")
                        else:
                            new_grid = times_checked - times_run
                            if new_grid == 0:
                                print("New grid saved\n")
                                data.append({self.campaign_name: {grid_name: self.grid}})
                                with open('JSON files/SavedGridData.json', 'w') as json_file:
                                    json.dump(data, json_file,
                                              indent=4,
                                              separators=(',', ': '))
                                return
                            else:
                                times_run += 1
                                pass

    def revert_grid(self):
        logging.debug('Prevents movement when moves in any direction are equal to boarder distance')
        logging.debug('Called in Location loop')
        if self.moves_UPDOWN > self.boarder_distance:
            self.move_south()
            logging.debug('Reverted grid north by one grid south')
        if self.moves_RIGHTLEFT > self.boarder_distance:
            self.move_west()
            logging.debug('Reverted grid east by one grid west')
        if self.moves_UPDOWN < -abs(self.boarder_distance):
            self.move_north()
            logging.debug('Reverted grid south by one grid north')
        if self.moves_RIGHTLEFT < -abs(self.boarder_distance):
            self.move_east()
            logging.debug('Reverted grid west by one grid east')
        if self.moves_UPDOWN >= self.boarder_distance or self.moves_UPDOWN <= -abs(
                self.boarder_distance) or self.moves_RIGHTLEFT >= self.boarder_distance or self.moves_RIGHTLEFT <= -abs(
                self.boarder_distance):
            self.approach_grid_movement = True

        else:
            self.approach_grid_movement = False
        self.player_movement()

    def move_north(self):
        if not self.approach_grid_movement:
            self.update_grid_north()
            self.randomize_grid_north()
            self.moves_UPDOWN += 1
        else:
            self.moves_UPDOWN += 1
            self.moves_UPDOWN_approach -= 1

    def move_east(self):
        if not self.approach_grid_movement:
            self.update_grid_east()
            self.randomize_grid_east()
            self.moves_RIGHTLEFT += 1
        else:
            self.moves_RIGHTLEFT += 1
            self.moves_RIGHTLEFT_approach += 1

    def move_south(self):
        if not self.approach_grid_movement:
            self.update_grid_south()
            self.randomize_grid_south()
            self.moves_UPDOWN -= 1
        else:
            self.moves_UPDOWN -= 1
            self.moves_RIGHTLEFT_approach += 1

    def move_west(self):
        if not self.approach_grid_movement:
            self.update_grid_west()
            self.randomize_grid_west()
            self.moves_RIGHTLEFT -= 1
        else:
            self.moves_RIGHTLEFT -= 1
            self.moves_RIGHTLEFT_approach -= 1

    # def approach_grid_movement(self):
    #     print("ran approach")
    #     if self.move_count == 5:
    #         self.move_count = 0
    #         print("Quick tip! You can save time by just imputing the initials of the direction you want to go in\n"
    #               "for example: n for north, ne for north east, etc...")
    #     move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
    #                  "east, south-east, south, south-west)\n")
    #     self.move_count += 1
    #     while True:
    #         if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west",
    #                     "north west", "north east", "south east", "south west", "n", "ne", "e", "se", "s", "sw", "w",
    #                     "nw"]:
    #             break
    #         else:
    #             move = input("Input invalid, please input a valid direction to move in.\nWhat direction would you "
    #                          "like to move in?\n(Options: west, north-west, north, north-east, east, south-east,
    #                          south, south-west)\n")
    #     if move == "west" or move == "w":
    #         self.moves_RIGHTLEFT -= 1
    #         self.moves_RIGHTLEFT_approach -= 1
    #     elif move == "north-west" or move == "north west" or move == "nw":
    #         self.moves_UPDOWN += 1
    #         self.moves_RIGHTLEFT -= 1
    #         self.moves_UPDOWN_approach -= 1
    #         self.moves_RIGHTLEFT_approach -= 1
    #     elif move == "north" or move == "n":
    #         self.moves_UPDOWN -= 1
    #         self.moves_UPDOWN_approach -= 1
    #     elif move == "north-east" or move == "north east" or move == "ne":
    #         self.moves_UPDOWN -= 1
    #         self.moves_RIGHTLEFT += 1
    #         self.moves_UPDOWN_approach -= 1
    #         self.moves_RIGHTLEFT_approach += 1
    #     elif move == "east" or move == "e":
    #         self.moves_RIGHTLEFT += 1
    #         self.moves_RIGHTLEFT_approach += 1
    #     elif move == "south-east" or move == "south east" or move == "se":
    #         self.moves_UPDOWN -= 1
    #         self.moves_RIGHTLEFT += 1
    #         self.moves_UPDOWN_approach += 1
    #         self.moves_RIGHTLEFT_approach += 1
    #     elif move == "south" or move == "s":
    #         self.moves_UPDOWN -= 1
    #         self.moves_UPDOWN_approach += 1
    #     elif move == "south-west" or move == "south west" or move == "sw":
    #         self.moves_UPDOWN -= 1
    #         self.moves_RIGHTLEFT -= 1
    #         self.moves_UPDOWN_approach -= 1
    #         self.moves_RIGHTLEFT_approach += 1
    #     else:
    #         while True:
    #             dev_funct = input("You are now in dev testing mode, what do you want to run: ")
    #             if dev_funct == "end":
    #                 break
    #     # self.set_boarder_location()
    #     self.revert_grid()

    def player_movement(self):
        print("ran movement")
        if self.move_count == 5:
            self.move_count = 0
            print("Quick tip! You can save time by just imputing the initials of the direction you want to go in"
                  "\nfor example: n for north, ne for north east, etc...")
        move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
                     "east, south-east, south, south-west)\n")
        self.move_count += 1
        while True:
            if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west",
                        "north west", "north east", "south east", "south west", "n", "ne", "e", "se", "s", "sw", "w",
                        "nw", "dev-7-8-22"]:
                break
            else:
                move = input("Input invalid, please input a valid direction to move in.\nWhat direction would you like"
                             " to move in?\n(Options: west, north-west, north, north-east, east, south-east, south, "
                             "south-west)\n")
        if move == "west" or move == "w":
            self.move_west()
        elif move == "north-west" or move == "north west" or move == "nw":
            self.move_north()
            self.move_west()
        elif move == "north" or move == "n":
            self.move_north()
        elif move == "north-east" or move == "north east" or move == "ne":
            self.move_north()
            self.move_east()
        elif move == "east" or move == "e":
            self.move_east()
        elif move == "south-east" or move == "south east" or move == "se":
            self.move_south()
            self.move_east()
        elif move == "south" or move == "s":
            self.move_south()
        elif move == "south-west" or move == "south west" or move == "sw":
            self.move_south()
            self.move_west()
        else:
            while True:
                dev_funct = input("You are now in dev testing mode, what do you want to run: ")
                if dev_funct == "end":
                    break
        self.set_location()

    def zo_locations(self):
        if self.update_temp_var == self.entrance:
            if self.ZO_location == "forest":
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[i])):
                        pass

    def clear_save_file(self):
        """
        Changes content of grid file to 0 to make it easier to delete its contents
        ONLY RUN TO CLEAR SAVED DATA IF YOU RUN THE PROGRAM WITH AN EMPTY FOLDER IT BREAKS
        """
        data = 0
        sf = json.dumps(data, indent=4, separators=(',', ': '))
        with open('JSON files/SavedGridData.json', "w") as outfile:
            outfile.write(sf)


#
loc = Location()
loc.get_data()
loc.create_location_grid(loc.visibility, loc.visibility)
loc.set_location()
loc.check_empty_file()
loc.print_location_grid()
print(loc.boarder_distance - abs(loc.moves_UPDOWN))
while True:
    print(f"Currently at: ({loc.moves_RIGHTLEFT}, {loc.moves_UPDOWN})")
    loc.revert_grid()
    loc.location_boarders(5)
    loc.save_grid()
    loc.print_location_grid()
