from collections import Counter

left_list: list[int] = []
right_list: list[int] = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(int(left))
        right_list.append(int(right))

left_list = sorted(left_list)
right_list = sorted(right_list)

# Part 1
total_distance = 0
combined = zip(left_list, right_list)
for left, right in combined:
    distance = abs(left - right)
    total_distance += distance

print("Total Distance (p1):", total_distance)

# Part 2
total_similarity = 0
right_count = Counter(right_list)

for i in left_list:
    total_similarity += i * right_count.get(i, 0)

print("Total Similarity (p2):", total_similarity)
