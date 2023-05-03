import json
import random
import Colors


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
        self.moves_UPDOWN_approach = 0
        self.moves_LEFTRIGHT = 0
        self.moves_LEFTRIGHT_approach = 0
        self.curr_pos = [self.moves_LEFTRIGHT, self.moves_UPDOWN]
        self.boarder_distance = 0
        self.campaign_name = ''
        self.distance_to_boarder_UPOWN = (self.boarder_distance - abs(self.moves_UPDOWN))
        self.distance_to_boarder_LEFTRIGHT = (self.boarder_distance - abs(self.moves_LEFTRIGHT))

    def assign_campaign_name(self, var, val):
        setattr(self, var, val)

    def set_location(self):
        self.grid[len(self.grid)//2][len(self.grid)//2] = self.player

    def set_boarder_location(self):
        if self.moves_LEFTRIGHT >= 0 or self.moves_UPDOWN >= 0:
            self.grid[0][0] = self.player

    def check_location(self):
        return self.ZO_location

    def change_location(self, new_location):
        pass

    def get_data(self):
        f = open('JSON files/Location_info.json')
        location_info_raw = f.read()
        location_info = json.loads(location_info_raw)
        self.location_data = location_info

    def create_location_grid(self, w, h):
        self.grid = []
        for i in range(w):
            row = []
            for j in range(h):
                row.append(self.empty_space)
            self.grid.append(row)
        self.randomize_grid()

    def print_location_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=' ')
            print()

    def increase_visibility(self):
        self.visibility += 2

    def decrease_visibility(self):
        self.visibility -= 2

    def randomize_grid(self):
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
        self.boarder_distance = boarder_distance
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.distance_to_boarder_UPOWN <= (self.visibility//2):
                    self.grid[(self.distance_to_boarder_UPOWN - (self.visibility//2))][j] = self.location_edge
                    # print(self.moves_UPDOWN)
                    # print("Reached location edge (north)")
                elif self.moves_LEFTRIGHT <= -abs(boarder_distance):
                    self.grid[i][0] = self.location_edge
                    # print(self.moves_LEFTRIGHT)
                    # print("Reached location edge (west)")
                elif self.moves_UPDOWN <= -abs(boarder_distance):
                    self.grid[len(self.grid)-1][j] = self.location_edge
                    # print(self.moves_UPDOWN)
                    # print("Reached location edge (south)")
                elif self.moves_LEFTRIGHT >= boarder_distance:
                    self.grid[i][len(self.grid)-1] = self.location_edge
                    # print(self.moves_LEFTRIGHT)
                    # print("Reached location edge (east)")
        if self.moves_UPDOWN >= boarder_distance or self.moves_UPDOWN <= -abs(
                boarder_distance) or self.moves_LEFTRIGHT >= self.boarder_distance or self.moves_LEFTRIGHT <= -abs(
                self.boarder_distance):
            self.approach_grid_movement()
        else:
            self.player_movement()

    def check_empty_file(self):
        with open("JSON files/SavedGridData.json", 'r') as f:
            one_char = f.read(1)
            if not one_char:
                data = [
                    {self.campaign_name: {"(" + str(self.moves_LEFTRIGHT) + "," + str(self.moves_UPDOWN) + ")": self.grid}}
                    ]
                sf = json.dumps(data, indent=4, separators=(',', ': '))
                with open('JSON files/SavedGridData.json', "w") as outfile:
                    outfile.write(sf)
                print("Created save 0")
            else:
                print("Passed grid save")
                self.save_grid()

    def save_grid(self):
        grid_name = "(" + str(self.moves_LEFTRIGHT) + "," + str(self.moves_UPDOWN) + ")"
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
        if self.moves_UPDOWN > self.boarder_distance:
            self.move_south()
        if self.moves_LEFTRIGHT > self.boarder_distance:
            self.move_west()
        if self.moves_UPDOWN > -abs(self.boarder_distance):
            self.move_north()
        if self.moves_LEFTRIGHT > -abs(self.boarder_distance):
            self.move_east()

    def move_north(self):
        self.update_grid_north()
        self.randomize_grid_north()
        self.moves_UPDOWN += 1

    def move_east(self):
        self.update_grid_east()
        self.randomize_grid_east()
        self.moves_LEFTRIGHT += 1

    def move_south(self):
        self.update_grid_south()
        self.randomize_grid_south()
        self.moves_UPDOWN -= 1

    def move_west(self):
        self.update_grid_west()
        self.randomize_grid_west()
        self.moves_LEFTRIGHT -= 1

    def approach_grid_movement(self):
        print("ran approach")
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
                        "nw"]:
                break
            else:
                move = input("Input invalid, please input a valid direction to move in.\nWhat direction would you like"
                             " to move in?\n(Options: west, north-west, north, north-east, east, south-east, south, "
                             "south-west)\n")
        if move == "west" or move == "w":
            self.moves_LEFTRIGHT -= 1
            self.moves_LEFTRIGHT_approach -= 1
        elif move == "north-west" or move == "north west" or move == "nw":
            self.moves_UPDOWN += 1
            self.moves_LEFTRIGHT -= 1
            self.moves_UPDOWN_approach += 1
            self.moves_LEFTRIGHT_approach -= 1
        elif move == "north" or move == "n":
            self.moves_UPDOWN += 1
            self.moves_UPDOWN_approach += 1
        elif move == "north-east" or move == "north east" or move == "ne":
            self.moves_UPDOWN += 1
            self.moves_LEFTRIGHT += 1
            self.moves_UPDOWN_approach += 1
            self.moves_LEFTRIGHT_approach += 1
        elif move == "east" or move == "e":
            self.moves_LEFTRIGHT += 1
            self.moves_LEFTRIGHT_approach += 1
        elif move == "south-east" or move == "south east" or move == "se":
            self.moves_UPDOWN -= 1
            self.moves_LEFTRIGHT += 1
            self.moves_UPDOWN_approach -= 1
        elif move == "south" or move == "s":
            self.moves_UPDOWN -= 1
            self.moves_UPDOWN_approach -= 1
        elif move == "south-west" or move == "south west" or move == "sw":
            self.moves_UPDOWN -= 1
            self.moves_LEFTRIGHT -= 1
            self.moves_UPDOWN_approach -= 1
            self.moves_LEFTRIGHT_approach -= 1
        else:
            while True:
                dev_funct = input("You are now in dev testing mode, what do you want to run: ")
                if dev_funct == "end":
                    break
        self.set_boarder_location()

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
        print(move)
        if move == "west" or move == "w":
            print("moved west")
            self.move_west()
        elif move == "north-west" or move == "north west" or move == "nw":
            print("moved north west")
            self.move_north()
            self.move_west()
        elif move == "north" or move == "n":
            print("moved north")
            self.move_north()
        elif move == "north-east" or move == "north east" or move == "ne":
            print("moved north east")
            self.move_north()
            self.move_east()
        elif move == "east" or move == "e":
            print("moved east")
            self.move_east()
        elif move == "south-east" or move == "south east" or move == "se":
            print("moved south east")
            self.move_south()
            self.move_east()
        elif move == "south" or move == "s":
            print("move south")
            self.move_south()
        elif move == "south-west" or move == "south west" or move == "sw":
            print("south west")
            self.move_south()
            self.move_west()
        else:
            while True:
                dev_funct = input("You are now in dev testing mode, what do you want to run: ")
                if dev_funct == "end":
                    break
        self.set_location()
        self.revert_grid()

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
loc.randomize_grid()
loc.set_location()
loc.check_empty_file()
loc.print_location_grid()
while True:
    print(f"Currently at: ({loc.moves_LEFTRIGHT}, {loc.moves_UPDOWN})")
    loc.location_boarders(5)
    print(-abs(loc.boarder_distance))
    loc.save_grid()
    loc.print_location_grid()
