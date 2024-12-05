safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        safe = True
        report = list(map(int, line.split()))

        sorted_report = sorted(report)
        if report != sorted_report:
            if report != sorted_report[::-1]:
                safe = False

        for idx, v in enumerate(report[1:]):
            distance = abs(v - report[idx])
            if distance not in (1, 2, 3):
                safe = False
                break

        if safe:
            safe_count += 1

# Part 1
print(safe_count)


# Part 2
def is_safe(report):
    sorted_report = sorted(report)
    if report != sorted_report:
        if report != sorted_report[::-1]:
            return False

    for idx, v in enumerate(report[1:]):
        distance = abs(v - report[idx])
        if distance not in (1, 2, 3):
            return False

    return True


safe_count_2 = 0
with open("input.txt", "r") as file:
    for line in file:
        safe = True
        report = list(map(int, line.split()))

        if not is_safe(report):
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]
                if is_safe(new_report):
                    safe = True
                    break
            else:
                safe = False

        if safe:
            safe_count_2 += 1

print(safe_count_2)
