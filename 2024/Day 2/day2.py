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
