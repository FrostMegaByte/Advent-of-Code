from itertools import product

with open("input.txt", "r") as file:
    lines = file.readlines()

# Part 1
total = 0
for line in lines:
    value_to_match, values = line.split(":")
    value_to_match = int(value_to_match.strip())
    values_list = list(map(int, values.strip().split()))
    operators = ["*", "+"]
    for ops in product(operators, repeat=len(values_list) - 1):
        parts = []
        for num, op in zip(values_list, ops + ("",)):
            parts.extend((num, op))
        parts.pop()
        result = int(parts[0])
        for i in range(1, len(parts), 2):
            operator = parts[i]
            next_value = int(parts[i + 1])
            if operator == "+":
                result += next_value
            elif operator == "*":
                result *= next_value

        if result == value_to_match:
            total += value_to_match
            break

print(total)

# Part 2
total_2 = 0
for line in lines:
    value_to_match, values = line.split(":")
    value_to_match = int(value_to_match.strip())
    values_list = list(map(int, values.strip().split()))
    operators = ["*", "+", "||"]
    for ops in product(operators, repeat=len(values_list) - 1):
        parts = []
        for num, op in zip(values_list, ops + ("",)):
            parts.extend((num, op))
        parts.pop()
        result = int(parts[0])
        for i in range(1, len(parts), 2):
            operator = parts[i]
            next_value = int(parts[i + 1])
            if operator == "+":
                result += next_value
            elif operator == "*":
                result *= next_value
            elif operator == "||":
                result = int(str(result) + str(parts[i + 1]))

        if result == value_to_match:
            total_2 += value_to_match
            break

# Takes ~40 seconds to run, but is correct
print(total_2)
