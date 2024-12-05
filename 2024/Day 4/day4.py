def find_xmas(grid):
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, diagonal down-right, diagonal down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, diagonal up-left, diagonal up-right
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    if all(0 <= r + i * dr < rows and 0 <= c + i * dc < cols and grid[r + i * dr][c + i * dc] == 'XMAS'[i] for i in range(4)):
                        count += 1
    return count

# def find_x_mas(grid):
#     directions = [
#         (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, diagonal down-right, diagonal down-left
#         (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, diagonal up-left, diagonal up-right
#     ]
#     count = 0
#     rows, cols = len(grid), len(grid[0])
    
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'M':
#                 for dr, dc in directions:
#                     if all(0 <= r + i * dr < rows and 0 <= c + i * dc < cols and grid[r + i * dr][c + i * dc] == 'MAS'[i] for i in range(3)):
#                         # Check the orthogonal diagonal
#                         a_x, a_y = r + dr, c + dc
#                         m_r1, m_c1 = a_x - dc, a_y + dr
#                         s_r1, s_c1 = a_x + dc, a_y - dr
#                         m_r2, m_c2 = a_x + dc, a_y - dr
#                         s_r2, s_c2 = a_x - dc, a_y + dr
#                         if (0 <= m_r1 < rows and 0 <= m_c1 < cols and 0 <= s_r1 < rows and 0 <= s_c1 < cols and
#                             grid[m_r1][m_c1] == 'M' and grid[s_r1][s_c1] == 'S'):
#                             count += 1
#                         elif (0 <= m_r2 < rows and 0 <= m_c2 < cols and 0 <= s_r2 < rows and 0 <= s_c2 < cols and
#                               grid[m_r2][m_c2] == 'S' and grid[s_r2][s_c2] == 'M'):
#                             count += 1
#     return count

def find_x_mas(grid):
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, diagonal down-right, diagonal down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, diagonal up-left, diagonal up-right
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                for dr, dc in directions:
                    if (0 <= r - dr < rows and 0 <= c - dc < cols and grid[r - dr][c - dc] == 'M' and
                        0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 'S'):
                        # Check the orthogonal diagonal
                        m_r1, m_c1 = r - dc, c + dr
                        s_r1, s_c1 = r + dc, c - dr
                        m_r2, m_c2 = r + dc, c - dr
                        s_r2, s_c2 = r - dc, c + dr
                        if (0 <= m_r1 < rows and 0 <= m_c1 < cols and 0 <= s_r1 < rows and 0 <= s_c1 < cols and
                            grid[m_r1][m_c1] == 'M' and grid[s_r1][s_c1] == 'S'):
                            count += 1
                        elif (0 <= m_r2 < rows and 0 <= m_c2 < cols and 0 <= s_r2 < rows and 0 <= s_c2 < cols and
                              grid[m_r2][m_c2] == 'S' and grid[s_r2][s_c2] == 'M'):
                            count += 1
    return count

# Example usage
with open('input.txt') as f:
    grid = [line.strip() for line in f]
    
# Part 1
# print(find_xmas(grid))

# Part 2
print(find_x_mas(grid))
