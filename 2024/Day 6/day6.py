import os


def parse_file_to_grid(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def find_guard_in_grid(grid):
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == '^':
                return (row_idx, col_idx), 'UP'
            elif col == '>':
                return (row_idx, col_idx), 'RIGHT'
            elif col == '<':
                return (row_idx, col_idx), 'LEFT'
            elif col == '∨':
                return (row_idx, col_idx), 'DOWN'

def create_shadow_copy(grid):
    return [row[:] for row in grid]

def move_guard(grid, location, direction):
    shadow_grid = create_shadow_copy(grid)
    row, col = location
    directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    direction_idx = directions.index(direction)
    
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        next_row, next_col = row, col
        if direction == 'UP':
            next_row -= 1
        elif direction == 'RIGHT':
            next_col += 1
        elif direction == 'DOWN':
            next_row += 1
        elif direction == 'LEFT':
            next_col -= 1
            
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            break
        if grid[next_row][next_col] == '#':
            direction_idx = (direction_idx + 1) % 4  # Rotate 90 degrees clockwise
            direction = directions[direction_idx]
        else:
            shadow_grid[row][col] = 'x'
            row, col = next_row, next_col
    
    return shadow_grid

# Part 1
grid = parse_file_to_grid("input.txt")
location, direction = find_guard_in_grid(grid)
shadow_grid = move_guard(grid, location, direction)
x_count = sum(row.count('x') for row in shadow_grid) + 1 # +1 to account for going outside the map bounds based on looking at next position