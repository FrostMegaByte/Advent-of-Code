import numpy as np


def parse_file_to_grid(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]


grid = parse_file_to_grid("input.txt")
antenna_locations = {}
for r_idx, row in enumerate(grid):
    for c_idx, char in enumerate(row):
        if char != "." and char != "#":
            if char not in antenna_locations:
                antenna_locations[char] = []
            antenna_locations[char].append((r_idx, c_idx))

# Part 1
anti_nodes = set()
for idx, loc in enumerate(antenna_locations):
    coordinates = antenna_locations[loc]
    for x in range(len(coordinates)):
        for y in range(x + 1, len(coordinates)):
            x1, y1 = coordinates[x]
            x2, y2 = coordinates[y]
            direction_distance = ((x2 - x1), (y2 - y1))
            new_loc_1 = np.subtract(coordinates[x], direction_distance)
            new_loc_2 = np.add(coordinates[y], direction_distance)
            if 0 <= new_loc_1[0] < len(grid) and 0 <= new_loc_1[1] < len(grid[0]):
                anti_nodes.add(tuple(new_loc_1))
            if 0 <= new_loc_2[0] < len(grid) and 0 <= new_loc_2[1] < len(grid[0]):
                anti_nodes.add(tuple(new_loc_2))

print(len(anti_nodes))

# Part 2
anti_nodes = set()
for idx, loc in enumerate(antenna_locations):
    coordinates = antenna_locations[loc]
    for x in range(len(coordinates)):
        for y in range(x + 1, len(coordinates)):
            x1, y1 = coordinates[x]
            x2, y2 = coordinates[y]
            direction_distance = np.array(((x2 - x1), (y2 - y1)))
            anti_nodes.add(tuple(coordinates[x]))
            anti_nodes.add(tuple(coordinates[y]))
            for i in range(1, len(grid)):
                new_loc_1 = np.subtract(coordinates[x], i * direction_distance)
                new_loc_2 = np.add(coordinates[y], i * direction_distance)
                if 0 <= new_loc_1[0] < len(grid) and 0 <= new_loc_1[1] < len(grid[0]):
                    anti_nodes.add(tuple(new_loc_1))
                if 0 <= new_loc_2[0] < len(grid) and 0 <= new_loc_2[1] < len(grid[0]):
                    anti_nodes.add(tuple(new_loc_2))

print(len(anti_nodes))
