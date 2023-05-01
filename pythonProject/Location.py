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
        self.moves_north = 0
        self.moves_west = 0
        self.moves_south = 0
        self.moves_east = 0
        self.curr_pos = [self.moves_east, self.moves_north]
        self.boarder_distance = 0
        self.campaign_name = ''

    def assign_campaign_name(self, var, val):
        setattr(self, var, val)

    def set_location(self):
        self.grid[len(self.grid)//2][len(self.grid)//2] = self.player

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

    def print_location_grid(self, g):
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
                if self.moves_north >= boarder_distance:
                    self.grid[0][j] = self.location_edge
                    print(self.moves_north)
                    print("Reached location edge (north)")
                if self.moves_west >= boarder_distance:
                    self.grid[i][0] = self.location_edge
                    print(self.moves_west)
                    print("Reached location edge (west)")
                if self.moves_south >= boarder_distance:
                    self.grid[len(self.grid)-1][j] = self.location_edge
                    print(self.moves_south)
                    print("Reached location edge (south)")
                if self.moves_east >= boarder_distance:
                    self.grid[i][len(self.grid)-1] = self.location_edge
                    print(self.moves_east)
                    print("Reached location edge (east)")

    def check_empty_file(self):
        with open("JSON files/SavedGridData.json", 'r') as f:
            one_char = f.read(1)
            if not one_char:
                data = [
                    {self.campaign_name: {"(" + str(self.moves_east) + "," + str(self.moves_north) + ")": self.grid}}
                    ]
                sf = json.dumps(data, indent=4, separators=(',', ': '))
                with open('JSON files/SavedGridData.json', "w") as outfile:
                    outfile.write(sf)
                print("Created save 0")
            else:
                print("Passed grid save")
                self.save_grid()

    def save_grid(self):
        grid_name = "(" + str(self.moves_east) + "," + str(self.moves_north) + ")"
        with open('JSON files/SavedGridData.json') as outfile:
            data = json.load(outfile)
            times_checked = len(data)
            times_run = 1
        for d in data:
            for key, value in d.items():
                for k, v in value.items():
                    if key == self.campaign_name:
                        print(f"k:{k}, grid_name:{grid_name}")
                        if k == grid_name:
                            print("found grid")
                            self.grid = v
                            print("grid loaded")
                        else:
                            print("Did not find grid")
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
        for p in reversed(range(len(self.grid))):
            for q in reversed(range(len(self.grid[p]))):
                if q != 0:
                    if self.grid[p][q - 1] == self.boarder_distance:
                        self.moves_east += 1
                        self.moves_west -= 1
                if p != 0:
                    if self.grid[p-1][q] == self.boarder_distance:
                        self.moves_north += 1
                        self.moves_south -= 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if j != len(self.grid) - 1:
                    if self.grid[i][j + 1] == self.boarder_distance:
                        self.moves_east -= 1
                        self.moves_west += 1
                if i != len(self.grid) - 1:
                    if self.grid[i + 1][j] == self.boarder_distance:
                        self.moves_south += 1
                        self.moves_north -= 1

    def move_north(self):
        self.update_grid_north()
        self.randomize_grid_north()
        self.moves_north += 1
        self.moves_south -= 1

    def move_east(self):
        self.update_grid_east()
        self.randomize_grid_east()
        self.moves_east += 1
        self.moves_west -= 1

    def move_south(self):
        self.update_grid_south()
        self.randomize_grid_south()
        self.moves_south += 1
        self.moves_north -= 1

    def move_west(self):
        self.update_grid_west()
        self.randomize_grid_west()
        self.moves_west += 1
        self.moves_east -= 1

    def player_movement(self):
        if self.move_count == 5:
            self.move_count = 0
            print("What direction would you like to move in?\n(Options: west, north-west, north, north-east, east,"
                  "south-east, south, south-west)")
            move = input("Quick tip! You can save time by just imputing the initials of the direction you want to go in"
                         "\nfor example: n for north, ne for north east, etc...\n")
            self.move_count += 1
        else:
            move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
                         "east, south-east, south, south-west)\n")
            self.move_count += 1
        if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west", "north "
                    "west", "north east", "south east", "south west", "n", "ne", "e", "se", "s", "sw", "w", "nw"]:
            if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west"]:
                if move == "west":
                    self.move_west()
                elif move == "north-west":
                    self.move_north()
                    self.move_west()
                elif move == "north":
                    self.move_north()
                elif move == "north-east":
                    self.move_north()
                    self.move_east()
                elif move == "east":
                    self.move_east()
                elif move == "south-east":
                    self.move_south()
                    self.move_east()
                elif move == "south":
                    self.move_south()
                elif move == "south-west":
                    self.move_south()
                    self.move_west()
            elif move in ["north west", "north east", "south east", "south west"]:
                if move == "north west":
                    self.move_north()
                    self.move_west()
                elif move == "north east":
                    self.move_north()
                    self.move_east()
                elif move == "south east":
                    self.move_south()
                    self.move_east()
                elif move == "south west":
                    self.move_south()
                    self.move_west()
            elif move in ["n", "ne", "e", "se", "s", "sw", "w", "nw"]:
                if move == "w":
                    self.move_west()
                elif move == "nw":
                    self.move_north()
                    self.move_west()
                elif move == "n":
                    self.move_north()
                elif move == "ne":
                    self.move_north()
                    self.move_east()
                elif move == "e":
                    self.move_east()
                elif move == "se":
                    self.move_south()
                    self.move_east()
                elif move == "s":
                    self.move_south()
                elif move == "sw":
                    self.move_south()
                    self.move_west()
        else:
            if move == "dev-7-8-22":
                while True:
                    dev_funct = input("You are now in dev testing mode, what do you want to run: ")
                    if dev_funct == "end":
                        break
            else:
                print("Please input a valid option.")
        self.set_location()
        # if 0 <= self.curr_pos[0] < len(self.grid) and 0 < self.curr_pos[1] <= len(self.grid):
        #     self.curr_pos = previous
        # else:
        # self.curr_pos = previous
        # self.update_grid()

    def zo_locations(self):
        if self.update_temp_var == self.entrance:
            if self.ZO_location == "forest":
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[i])):
                        pass


#
loc = Location()
loc.get_data()
loc.create_location_grid(loc.visibility, loc.visibility)
loc.location_boarders(5)
loc.randomize_grid()
loc.set_location()
loc.check_empty_file()
loc.print_location_grid(loc.grid)
while True:
    print(f"Currently at: ({loc.moves_east}, {loc.moves_north})")
    loc.player_movement()
    loc.revert_grid()
    loc.save_grid()
    loc.location_boarders(5)
    loc.print_location_grid(loc.grid)
