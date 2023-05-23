import json
import random
import Colors
import logging
logging.basicConfig(level=logging.DEBUG, filename='Location-debug.log')


class Location:
    def __init__(self):
        self.player = "[" + Colors.BLUE + "@" + Colors.END + "]"
        self.empty_space = "   "
        self.enemy = "[" + Colors.RED + "E" + Colors.END + "]"
        self.tree = "[" + Colors.GREEN + "T" + Colors.END + "]"
        self.location_edge = "   "
        self.entrance = Colors.WHITE + "[E]" + Colors.END
        self.out_of_vision = Colors.WHITE + "[ ]" + Colors.END
        self.grid = []
        self.location_data = ""
        self.ZO_location = "Forest"
        self.move_count = 9
        self.visibility = 41
        self.update_temp_var = self.empty_space
        self.moves_UPDOWN = 0
        self.moves_UPDOWN_approach = 0
        self.moves_RIGHTLEFT = 0
        self.moves_RIGHTLEFT_approach = 0
        self.curr_pos = [self.moves_RIGHTLEFT, self.moves_UPDOWN]
        self.boarder_distance = 0
        self.campaign_name = ''
        self.distance_to_boarder_UPOWN = self.boarder_distance
        self.distance_to_boarder_RIGHTLEFT = self.boarder_distance
        self.approach_grid_movement_UPDOWN = False
        self.approach_grid_movement_RIGHTLEFT = False
        self.approach_moves_north = 0
        self.approach_moves_east = 1
        self.approach_moves_south = 1
        self.approach_moves_west = 1
        logging.debug('__init__ accessed')

    def assign_campaign_name(self, var, val):
        """
        Takes the campaign name from Game Control and applies it here so when you save or load campaigns on Game Control
        it loads it here as well
        """
        logging.debug('Assign_campaign_name called')
        logging.debug('Assigned campaign name')
        logging.debug('Called from Game_control')
        setattr(self, var, val)

    def set_boarder_approach_location(self):
        self.moves_UPDOWN_approach = (len(self.grid) // 2)
        self.moves_RIGHTLEFT_approach = (len(self.grid) // 2)

    def set_location(self):
        """
        Sets the center of the grid to self.player
        """
        logging.debug('Set_location called')
        logging.debug('Set location to middle of graph')
        logging.debug('Called from self.player_movement()')
        self.grid[len(self.grid)//2][len(self.grid)//2] = self.player

    def set_boarder_location(self):
        logging.debug('Set_boarder_location called')
        logging.debug(f'Setting [P] <player> to coordinates ({self.moves_RIGHTLEFT_approach}, '
                      f'{self.moves_UPDOWN_approach})')
        logging.debug('Called for self.player_movement()')
        self.grid[len(self.grid) // 2][len(self.grid) // 2] = self.update_temp_var
        self.grid[self.moves_UPDOWN_approach][self.moves_RIGHTLEFT_approach] = self.player
        print(f"{self.moves_RIGHTLEFT_approach}, {self.moves_UPDOWN_approach}")

    def check_location(self):
        """

        """
        logging.debug('Unfinished function')
        return self.ZO_location

    def change_location(self, new_location):
        """

        :param new_location:
        """
        logging.debug('Unfinished function')
        pass

    def get_data(self):
        """
        Takes data from the Location_info.json document and applies it all to self.location_data
        """
        logging.debug('Get_data called')
        logging.debug('Taking data for Location descriptions and assigning it to self.location_data')
        logging.debug('Called at the beginning of Location run')
        f = open('JSON files/Location_info.json')
        location_info_raw = f.read()
        location_info = json.loads(location_info_raw)
        self.location_data = location_info

    def create_location_grid(self, s):
        """
        Creates a w by h grid using for loops and appends self.empty_space ([ ]) to each grid space
        :param s: The size of the grid
        """
        logging.debug('create_location_grid called')
        logging.debug('Creating a grid with specified s <size>')
        logging.debug('Called at the beginning of Location run')
        self.grid = []
        for i in range(s):
            row = []
            for j in range(s):
                row.append(self.empty_space)
            self.grid.append(row)
        self.randomize_grid("All")

    def print_location_grid(self):
        """
        Prints out the grid created bby self.create_location_grid with any changes applied by later functions
        """
        logging.debug('print_location_grid called')
        logging.debug('Printing out the grid')
        logging.debug('Called at the beginning of Location run and end of every loop')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=' ')
            print()

    def increase_visibility(self):
        """
        Increases the size of the grid by 2 spaces in order to keep the existence of a perfect center (equal grid spaces
        on all sides)
        """
        logging.debug('Increase_visibility called')
        logging.debug('Increasing visibility by 2 grid spaces')
        self.visibility += 2

    def decrease_visibility(self):
        """
        Decreases the size of the grid by 2 spaces in order to keep the existence of a perfect center (equal grid spaces
        on all sides)
        """
        logging.debug('Decrease_visibility called')
        logging.debug('Decreasing visibility by 2 grid spaces')
        self.visibility -= 2

    def randomize_grid(self, direction):
        """
        Assigns random predefined variables to random grid spaces from the grid created in self.create_location_grid
        """
        logging.debug('Randomize_grid called')
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
                if direction == "All":
                    self.grid[i][j] = random_gen
                elif direction == "North":
                    self.grid[0][j] = random_gen
                elif direction == "East":
                    self.grid[i][0] = random_gen
                elif direction == "South":
                    self.grid[len(self.grid) - 1][j] = random_gen
                elif direction == "West":
                    self.grid[i][len(self.grid) - 1] = random_gen

    def update_grid(self, direction):
        if not self.approach_grid_movement_UPDOWN:
            for i in reversed(range(len(self.grid))):
                for j in reversed(range(len(self.grid[i]))):
                    if direction == "North":
                        if i != 0:
                            if self.grid[i - 1][j] == self.player:
                                self.grid[(len(self.grid) // 2) + 1][len(self.grid) // 2] = self.update_temp_var
                                self.update_temp_var = self.grid[(len(self.grid) // 2) - 1][len(self.grid) // 2]
                            else:
                                self.grid[i][j] = self.grid[i - 1][j]
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if direction == "South":
                        if i != len(self.grid) - 1:
                            if self.grid[i + 1][j] == self.player:
                                self.grid[(len(self.grid) // 2) - 1][len(self.grid) // 2] = self.update_temp_var
                                self.update_temp_var = self.grid[(len(self.grid) // 2) + 1][(len(self.grid)) // 2]
                            else:
                                self.grid[i][j] = self.grid[i + 1][j]
        else:
            for i in reversed(range(len(self.grid))):
                for j in reversed(range(len(self.grid[i]))):
                    if direction == "North":
                        print("moved north")
                        if i != 0:
                            if self.grid[i - 1][j] == self.player:
                                self.grid[
                                    self.moves_UPDOWN_approach + 1][
                                    self.moves_UPDOWN_approach] = self.update_temp_var
                                self.update_temp_var = self.grid[
                                    self.moves_UPDOWN_approach - 1][
                                    self.moves_UPDOWN_approach]
                            else:
                                self.grid[i][j] = self.grid[i - 1][j]
                            self.grid[(len(self.grid) - 1) - self.approach_moves_north][j] = self.out_of_vision
                    if direction == "South":
                        print("moved south")
                        if i != len(self.grid) - 1:
                            if self.grid[i + 1][j] == self.player:
                                self.grid[
                                    self.moves_UPDOWN_approach][
                                    self.moves_UPDOWN_approach - 1] = self.update_temp_var
                                self.update_temp_var = self.grid[
                                    self.moves_UPDOWN_approach][
                                    self.moves_UPDOWN_approach + 1]
                            else:
                                self.grid[i][j] = self.grid[i + 1][j]
                            self.grid[(len(self.grid) - 1) - ((len(self.grid) - 1) - self.approach_moves_south)][
                                j] = self.out_of_vision
        if not self.approach_grid_movement_RIGHTLEFT:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if direction == "East":
                        if j != len(self.grid) - 1:
                            if self.grid[i][j + 1] == self.player:
                                self.grid[len(self.grid) // 2][(len(self.grid) // 2) - 1] = self.update_temp_var
                                self.update_temp_var = self.grid[len(self.grid) // 2][((len(self.grid)) // 2) + 1]
                            else:
                                self.grid[i][j] = self.grid[i][j + 1]
            for i in reversed(range(len(self.grid))):
                for j in reversed(range(len(self.grid[i]))):
                    if direction == "West":
                        if j != 0:
                            if self.grid[i][j - 1] == self.player:
                                self.grid[len(self.grid) // 2][(len(self.grid) // 2) + 1] = self.update_temp_var
                                self.update_temp_var = self.grid[(len(self.grid)) // 2][(len(self.grid) // 2) - 1]
                            else:
                                self.grid[i][j] = self.grid[i][j - 1]
        else:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if direction == "East":
                        print("moved east")
                        if j != len(self.grid) - 1:
                            if self.grid[i][j + 1] == self.player:
                                self.grid[
                                    self.moves_RIGHTLEFT_approach][
                                    self.moves_RIGHTLEFT_approach - 1] = self.update_temp_var
                                self.update_temp_var = self.grid[
                                    self.moves_RIGHTLEFT_approach][
                                    self.moves_RIGHTLEFT_approach + 1]
                            else:
                                self.grid[i][j] = self.grid[i][j + 1]
                            self.grid[i][(len(self.grid) - 1) - (
                                        (len(self.grid) - 1) - self.approach_moves_east)] = self.out_of_vision
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if direction == "West":
                        print("moved west")
                        if self.grid[i][j] == self.player:
                            self.grid[
                                self.moves_RIGHTLEFT_approach - 1][
                                self.moves_RIGHTLEFT_approach] = self.update_temp_var
                            self.update_temp_var = self.grid[
                                self.moves_RIGHTLEFT_approach + 1][
                                self.moves_RIGHTLEFT_approach]
                        else:
                            self.grid[i][j] = self.grid[i][j - 1]
                        self.grid[i][(len(self.grid) - 1) - (
                                    (len(self.grid) - 1) - self.approach_moves_west)] = self.out_of_vision

    def location_boarders(self, boarder_distance):
        """
        Sets a distance after which the player encounters a 'boarder' that they cant cross, it also prints out this
        boarder whenever the player gets close to it.
        :param boarder_distance: How far a player can move before reaching the boarder
        """
        logging.debug('Location_boarders called')
        logging.debug('Assigns border distance, assigns it to self.boarder distance, and creates boarders where needed')
        logging.debug('Called in Location loop after self.revert_grid')
        self.boarder_distance = boarder_distance
        self.distance_to_boarder_UPOWN = (boarder_distance - abs(self.moves_UPDOWN))
        self.distance_to_boarder_RIGHTLEFT = (boarder_distance - abs(self.moves_RIGHTLEFT))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.distance_to_boarder_UPOWN < -abs(self.visibility//2):
                    self.approach_grid_movement_UPDOWN = True
                elif self.distance_to_boarder_UPOWN < (self.visibility//2):
                    self.approach_grid_movement_UPDOWN = True
                else:
                    self.approach_grid_movement_UPDOWN = False
                if self.distance_to_boarder_RIGHTLEFT < -abs(self.visibility//2):
                    self.approach_grid_movement_RIGHTLEFT = True
                elif self.distance_to_boarder_RIGHTLEFT < self.visibility//2:
                    self.approach_grid_movement_RIGHTLEFT = True
                else:
                    self.approach_grid_movement_RIGHTLEFT = False

    def check_empty_file(self):
        """
        Checks the SavedGridData.Json for content and if it contains any it replaces it with a '0' in order to make it
        easy to delete and clear the documents data
        """
        logging.debug('Check_empty_file called')
        logging.debug('Checks file for characters, if the file is empty it creates a new save, otherwise it runs '
                      'self.save_grid')
        logging.debug('Called only for the purpose of clearing SavedGridData.json')
        with open("JSON files/SavedGridData.json", 'r') as f:
            one_char = f.read(1)
            if not one_char or one_char == '0':
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
        """
        Saves the grid and its content to the campaign name and coordinates and loads the same grid if the campaign name
        and coordinates match
        """
        logging.debug('Save_grid called')
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
        """
        Prevents player movement past the boarder '[#]'
        """
        logging.debug('Revert_grid called')
        logging.debug('Prevents movement when moves in any direction are equal to boarder distance')
        logging.debug('Called in Location loop')
        if self.moves_UPDOWN > self.boarder_distance:
            self.move_south()
            logging.debug('Reverted grid north by one grid south')
        if self.moves_RIGHTLEFT_approach > self.boarder_distance:
            self.move_west()
            logging.debug('Reverted grid east by one grid west')
        if self.moves_UPDOWN_approach < -abs(self.boarder_distance):
            self.move_north()
            logging.debug('Reverted grid south by one grid north')
        if self.moves_RIGHTLEFT_approach < -abs(self.boarder_distance):
            self.move_east()
            logging.debug('Reverted grid west by one grid east')

    def move_north(self):
        """
        Triggers either the self.update and self.randomize _grid_north() and moves
        """
        logging.debug('Move_north called')
        if not self.approach_grid_movement_UPDOWN:
            logging.debug("ran player movement")
            print("movement")
            self.update_grid("North")
            self.randomize_grid("North")
            self.moves_UPDOWN += 1
            self.approach_moves_north = 0
        else:
            logging.debug("ran player approach")
            print("approach")
            self.update_grid("North")
            self.moves_UPDOWN += 1
            self.moves_UPDOWN_approach -= 1
            if self.approach_moves_north < self.visibility//2:
                self.approach_moves_north += 1

    def move_east(self):
        logging.debug('Move_east called')
        if not self.approach_grid_movement_RIGHTLEFT:
            logging.debug("ran player movement")
            print("movement")
            self.update_grid("East")
            self.randomize_grid("East")
            self.moves_RIGHTLEFT += 1
        else:
            logging.debug("ran player approach")
            print("approach")
            if self.moves_RIGHTLEFT_approach < (len(self.grid) - 1):
                self.update_grid("East")
                self.moves_RIGHTLEFT += 1
                self.moves_RIGHTLEFT_approach += 1

    def move_south(self):
        logging.debug('Move_south called')
        if not self.approach_grid_movement_UPDOWN:
            logging.debug("ran player movement")
            print("movement")
            self.update_grid("South")
            self.randomize_grid("South")
            self.moves_UPDOWN -= 1
        else:
            logging.debug("ran player approach")
            print("approach")
            if self.moves_UPDOWN_approach < (len(self.grid) - 1):
                self.update_grid("South")
                self.moves_UPDOWN -= 1
                self.moves_UPDOWN_approach += 1

    def move_west(self):
        logging.debug('Move_west called')
        if not self.approach_grid_movement_RIGHTLEFT:
            logging.debug("ran player movement")
            print("movement")
            self.update_grid("West")
            self.randomize_grid("West")
            self.moves_RIGHTLEFT -= 1
        else:
            logging.debug("ran player approach")
            print("approach")
            if self.moves_RIGHTLEFT_approach > 0:
                self.update_grid("West")
                self.moves_RIGHTLEFT -= 1
                self.moves_RIGHTLEFT_approach -= 1

    def player_movement(self):
        logging.debug('Player_movement called')
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
        self.revert_grid()

    def zo_locations(self):
        logging.debug('ZO_locations called')
        if self.update_temp_var == self.entrance:
            if self.ZO_location == "forest":
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[i])):
                        pass

    def set_player_pos(self):
        if self.approach_grid_movement_UPDOWN or self.approach_grid_movement_RIGHTLEFT:
            self.set_boarder_location()
        else:
            self.set_location()

    def clear_save_file(self):
        """
        Changes content of grid file to 0 to make it easier to delete its contents
        ONLY RUN TO CLEAR SAVED DATA IF YOU RUN THE PROGRAM WITH AN EMPTY FOLDER IT BREAKS
        """
        logging.debug('Clear_save_file called')
        data = 0
        sf = json.dumps(data, indent=4, separators=(',', ': '))
        with open('JSON files/SavedGridData.json', "w") as outfile:
            outfile.write(sf)

    def generate_biomes(self, biome, size):
        biome_center = []
        if biome == "desert":
            biome = Colors.YELLOW2 + "[ ]" + Colors.END
        biome_center = [random.randint(0, 40), random.randint(0, 40)]
        print(biome_center)
        while True:
            if biome_center[0] - size//2 < 0 or biome_center[0] + size//2 > 40:
                biome_center = [random.randint(0, 40), random.randint(0, 40)]
            else:
                pass
            if biome_center[1] - size//2 < 0 or biome_center[1] + size//2 > 40:
                biome_center = [random.randint(0, 40), random.randint(0, 40)]
            else:
                break
        for row in range(biome_center[0] - size//2, biome_center[0] + size//2):
            for col in range(biome_center[1] - size//2, biome_center[1] + size//2):
                if self.grid[row][col] == "   ":
                    self.grid[row][col] = biome
                if self.grid[row][col] == self.tree:
                    desert_tree = Colors.YELLOW2 + "[" + Colors.END + Colors.GREEN + "T" + Colors.END + Colors.YELLOW2 + "]" + Colors.END
                    self.grid[row][col] = desert_tree
                if self.grid[row][col] == self.enemy:
                    desert_enemy = Colors.YELLOW2 + "[" + Colors.END + Colors.RED + "E" + Colors.END + Colors.YELLOW2 + "]" + Colors.END
                    self.grid[row][col] = desert_enemy
        # ISSUES TO FIX STILL 1. The biomes are affected by movement, ex. if you move north the biome will move as well
        # General quality of life issues and color scheme for the content


#
loc = Location()
loc.clear_save_file()
loc.get_data()
loc.create_location_grid(loc.visibility)
loc.set_location()
loc.check_empty_file()
loc.generate_biomes("desert", 5)
loc.generate_biomes("desert", 10)
loc.generate_biomes("desert", 12)
loc.generate_biomes("desert", 2)
loc.print_location_grid()
loc.set_boarder_approach_location()
loc.location_boarders(200)
while True:
    print(f"Currently at: ({loc.moves_RIGHTLEFT}, {loc.moves_UPDOWN})")
    loc.player_movement()
    loc.location_boarders(200)
    loc.save_grid()
    loc.set_player_pos()
    loc.print_location_grid()