from collections import deque

with open("input.txt", "r") as file:
    line = file.readline()
    instructions = [int(c) for c in line]

q = deque()
string_in_full = ""
id = 0
for i in range(0, len(instructions), 2):
    file_size = instructions[i]
    if i + 1 < len(instructions):
        free_space = instructions[i + 1]
    else:
        free_space = 0

    for i in range(file_size):
        q.append(str(id))
        string_in_full += str(id)
    for i in range(free_space):
        q.append(".")
        string_in_full += "."
    id += 1

left = 0
right = len(string_in_full) - 1
result = []

while left <= right:
    if string_in_full[left] != ".":
        result.append(string_in_full[left])
        left += 1
    else:
        if string_in_full[right] != ".":
            result.append(string_in_full[right])
            right -= 1
        else:
            while string_in_full[right] == ".":
                right -= 1
            result.append(string_in_full[right])
            right -= 1
        left += 1

total = 0
for index, value in enumerate(result):
    total += index * int(value)

print(total)
