def parse_file(filepath):
    with open(filepath, "r") as file:
        content = file.read().strip()

    rules_part, updates_part = content.split("\n\n")

    rules = set()
    for line in rules_part.split("\n"):
        a, b = map(int, line.split("|"))
        rules.add((a, b))

    updates = []
    for line in updates_part.split("\n"):
        updates.append(list(map(int, line.split(","))))

    return rules, updates


# Example usage
rules, updates = parse_file("input.txt")

# Part 1
total = 0
for update in updates:
    valid = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            ordering = (update[i], update[j])
            if ordering not in rules:
                valid = False

    # Find the middle value in the update
    if valid:
        middle_index = len(update) // 2
        middle_value = update[middle_index]
        total += middle_value

print(total)


# Some form of recursion. I find it ugly, but it works
def correct_update_order(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            ordering = (update[i], update[j])
            if ordering not in rules:
                update[i], update[j] = update[j], update[i]
                update, _ = correct_update_order(update)
                return update, False
    return update, True


# Part 2
total_2 = 0
for update in updates:
    update, was_initially_correct = correct_update_order(update)
    if not was_initially_correct:
        total_2 += update[len(update) // 2]

print(total_2)
