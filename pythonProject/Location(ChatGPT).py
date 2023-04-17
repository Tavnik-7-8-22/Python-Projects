def create_grid(width, height):
    """Creates a grid with the given width and height."""
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append('.')
        grid.append(row)
    return grid

def print_grid(grid):
    """Prints the grid."""
    for row in grid:
        print(' '.join(row))

def move_player(grid, player_position, direction):
    """Moves the player in the given direction."""
    x, y = player_position
    if direction == 'up':
        y -= 1
    elif direction == 'down':
        y += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        grid[player_position[1]][player_position[0]] = '.'
        player_position = (x, y)
        grid[player_position[1]][player_position[0]] = 'P'
    return player_position

def main():
    """Runs the main program."""
    width = int(input('Enter grid width: '))
    height = int(input('Enter grid height: '))
    grid = create_grid(width, height)
    player_position = (0, 0)
    grid[player_position[1]][player_position[0]] = 'P'
    print_grid(grid)
    while True:
        direction = input('Enter direction (up/down/left/right): ')
        player_position = move_player(grid, player_position, direction)
        print_grid(grid)

if __name__ == '__main__':
    main()
