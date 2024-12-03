import re

total = 0
multiply_flag = True

with open("input.txt", "r") as file:
    for line in file:
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                multiply_flag = True
                continue
            if match == "don't()":
                multiply_flag = False
                continue

            numbers = re.findall(r"\d{1,3}", match)
            if numbers and multiply_flag:
                result = int(numbers[0]) * int(numbers[1])
                total += result

print(total)
