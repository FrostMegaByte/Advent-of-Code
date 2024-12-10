
def parse_file(filepath):
    with open(filepath, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]
    return grid

def find_zeros(grid):
    zeros = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 0:
                zeros.append((i, j))
    return zeros

def find_paths_1(grid, start):
    paths = []
    stack = [(start, [start])]
    reached_top = set()
    while stack:
        (x, y), path = stack.pop()
        if grid[x][y] == 9:
            if (x, y) not in reached_top:
                paths.append(path)
                reached_top.add((x, y))
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in path:
                if grid[nx][ny] == grid[x][y] + 1:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return paths

def find_paths_2(grid, start):
    paths = []
    stack = [(start, [start])]
    while stack:
        (x, y), path = stack.pop()
        if grid[x][y] == 9:
            paths.append(path)
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in path:
                if grid[nx][ny] == grid[x][y] + 1:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return paths

# Part 1
def main1():
    filepath = 'input.txt'
    grid = parse_file(filepath)
    zeros = find_zeros(grid)
    all_paths = []
    for zero in zeros:
        paths = find_paths_1(grid, zero)
        all_paths.extend(paths)
    print(f"Total paths found: {len(all_paths)}")

# Part 2
def main2():
    filepath = 'input.txt'
    grid = parse_file(filepath)
    zeros = find_zeros(grid)
    all_paths = []
    for zero in zeros:
        paths = find_paths_2(grid, zero)
        all_paths.extend(paths)
    print(f"Total paths found: {len(all_paths)}")

if __name__ == "__main__":
    main1()
    main2()