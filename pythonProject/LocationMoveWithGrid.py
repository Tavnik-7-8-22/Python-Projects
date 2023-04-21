import json
import random
import Colors


class Location:
    def __init__(self):
        self.player = "[" + Colors.GREEN + "P" + Colors.END + "]"
        self.empty_space = "[ ]"
        self.enemy = "[" + Colors.RED + "E" + Colors.END + "]"
        self.tree = "[" + Colors.GREEN2 + "T" + Colors.END + "]"
        self.barrier = "#"
        # self.start = [1, 1]
        self.curr_pos = [1, 1]
        # self.prev_pos = self.start
        self.grid = []
        self.location_data = ""
        self.move_count = 5
        self.visibility = 3

    def set_location(self):
        for i in range(len(self.grid)):
            for j in range(len((self.grid[i]))):
                self.curr_pos = [int(len(loc.grid)/2), int(len(loc.grid)/2)]

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

    # def update_grid(self):
    #     # self.grid[self.prev_pos[0]][self.prev_pos[1]] = self.empty_space
    #     col = self.curr_pos[0]
    #     row = self.curr_pos[1]
    #     if row <= 0:
    #         self.curr_pos[1] = 0
    #     if col <= 0:
    #         self.curr_pos[0] = 0
    #     if col >= len(self.grid):
    #         self.curr_pos[0] = len(self.grid) - 1
    #     if row >= len(self.grid[0]):
    #         self.curr_pos[1] = len(self.grid[0]) - 1
    #
    #     self.grid[self.curr_pos[0]][self.curr_pos[1]] = self.player
    #     col = self.curr_pos[0]
    #     row = self.curr_pos[1]
    #     print(*self.location_data["Forest"][self.curr_pos[0]][self.curr_pos[1]].values())

    def print_location_grid(self, g):
        for i in range(len(g)):
            for j in range(len(g[i])):
                print(g[i][j], end=' ')
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
        self.grid[self.curr_pos[0]][self.curr_pos[1]] = self.player

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
                    self.grid[i][j] = random_gen

    def randomize_grid_east(self):
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

    def randomize_grid_west(self):
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
                if i != 0:
                    # print(self.grid[i][j])
                    # print(self.grid[i-1][j])
                    if self.grid[i-1][j] == self.player:
                        self.grid[i][j] = self.empty_space
                    else:
                        self.grid[i][j] = self.grid[i - 1][j]

    def player_movement(self):
        if self.move_count > 5:
            self.move_count = 0
            move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
                         "east, south-east, south, south-west)\n")
            self.move_count += 1
        elif self.move_count == 5:
            print("What direction would you like to move in?\n(Options: west, north-west, north, north-east, east,"
                  "south-east, south, south-west)")
            move = input("Quick tip! You can save time by just imputing the initials of the direction you want to go in"
                         "\nfor example: n for north, ne for north east, etc...\n")
            self.move_count += 1
        else:
            move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
                         "east, south-east, south, south-west)\n")
            self.move_count += 1
        # previous = self.curr_pos
        if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west", "north "
                    "west", "north east", "south east", "south west", "n", "ne", "e", "se", "s", "sw", "w", "nw"]:
            if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west"]:
                if move == "west":
                    self.randomize_grid_west()
                elif move == "north-west":
                    self.randomize_grid_north()
                    self.randomize_grid_west()
                elif move == "north":
                    self.update_grid_north()
                    self.randomize_grid_north()
                elif move == "north-east":
                    self.randomize_grid_north()
                    self.randomize_grid_east()
                elif move == "east":
                    self.randomize_grid_east()
                elif move == "south-east":
                    self.randomize_grid_south()
                    self.randomize_grid_east()
                elif move == "south":
                    self.randomize_grid_south()
                elif move == "south-west":
                    self.randomize_grid_south()
                    self.randomize_grid_west()
            elif move in ["north west", "north east", "south east", "south west"]:
                if move == "north west":
                    self.randomize_grid_north()
                    self.randomize_grid_west()
                elif move == "north east":
                    self.randomize_grid_north()
                    self.randomize_grid_east()
                elif move == "south east":
                    self.randomize_grid_south()
                    self.randomize_grid_east()
                elif move == "south west":
                    self.randomize_grid_south()
                    self.randomize_grid_west()
            elif move in ["n", "ne", "e", "se", "s", "sw", "w", "nw"]:
                if move == "w":
                    self.randomize_grid_west()
                elif move == "nw":
                    self.randomize_grid_north()
                    self.randomize_grid_west()
                elif move == "n":
                    self.randomize_grid_north()
                elif move == "ne":
                    self.randomize_grid_north()
                    self.randomize_grid_east()
                elif move == "e":
                    self.randomize_grid_east()
                elif move == "se":
                    self.randomize_grid_south()
                    self.randomize_grid_east()
                elif move == "s":
                    self.randomize_grid_south()
                elif move == "sw":
                    self.randomize_grid_south()
                    self.randomize_grid_west()
        else:
            if move == "dev-7-8-22":
                while True:
                    devtrig = input("You are now in dev testing mode, what do you want to run: ")
                    if devtrig == "end":
                        break
            else:
                print("Please input a valid option.")
        self.grid[self.curr_pos[0]][self.curr_pos[1]] = self.player
        # if 0 <= self.curr_pos[0] < len(self.grid) and 0 < self.curr_pos[1] <= len(self.grid):
        #     self.curr_pos = previous
        # else:
        # self.curr_pos = previous
        # self.update_grid()


loc = Location()
loc.get_data()
loc.create_location_grid(3, 3)
loc.set_location()
loc.randomize_grid()
loc.print_location_grid(loc.grid)
while True:
    loc.player_movement()
    loc.print_location_grid(loc.grid)
# loc.get_data()
# print('Current Position: {}'.format(loc.curr_pos))
# print(*loc.location_data["Forest"][loc.curr_pos[0]][loc.curr_pos[1]].values())
# # print('Previous Position: {}'.format(loc.prev_pos))
# loc.create_location_grid(3, 3)
# # loc.update_grid()
# loc.print_location_grid(loc.grid)
# while True:
#     loc.player_movement()
#     loc.update_grid()
#     print('Current Position: {}'.format(loc.curr_pos))
#     # print(*loc.location_data["Location"][0][loc.curr_pos[0]][loc.curr_pos[1]].values())
#     # print('Previous Position: {}'.format(loc.prev_pos))
#     # loc.update_grid()
#     loc.create_location_grid(3, 3)
#     loc.print_location_grid(loc.grid)
