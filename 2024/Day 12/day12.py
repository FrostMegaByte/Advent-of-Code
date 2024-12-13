class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


def parse_file(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def find_connected_components(grid):
    if not grid:
        return []

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)

    def index(r, c):
        return r * cols + c

    for r in range(rows):
        for c in range(cols):
            if r > 0 and grid[r][c] == grid[r - 1][c]:
                uf.union(index(r, c), index(r - 1, c))
            if c > 0 and grid[r][c] == grid[r][c - 1]:
                uf.union(index(r, c), index(r, c - 1))

    components = {}
    for r in range(rows):
        for c in range(cols):
            root = uf.find(index(r, c))
            char = grid[r][c]
            if char not in components:
                components[char] = {}
            if root not in components[char]:
                components[char][root] = []
            components[char][root].append((r, c))

    return components


def calculate_perimeter_and_area(component):
    area = len(component)
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in component:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in component:
                perimeter += 1

    return area, perimeter


def calculate_sides(component):
    pass


# Parse the file
filename = "small1.txt"
grid = parse_file(filename)

# Find connected components
components = find_connected_components(grid)

# Part 1
total_1 = 0
# Calculate and print the perimeter and area for each component
for char, groups in components.items():
    for root, cells in groups.items():
        area, perimeter = calculate_perimeter_and_area(set(cells))
        total_1 += area * perimeter
print(total_1)


# Part 2
total_2 = 0
# Calculate and print the number of sides for each component
for char, groups in components.items():
    for root, cells in groups.items():
        sides = calculate_sides(set(cells))
        area = len(set(cells))
        total_2 += sides * area
print(total_2)
