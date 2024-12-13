import sympy as sp


def parse_line(line):
    parts = line.split(": ")[1].split(", ")
    x = int(parts[0].split("+")[1])
    y = int(parts[1].split("+")[1])
    return x, y


def parse_prize(line):
    parts = line.split(": ")[1].split(", ")
    x = int(parts[0].split("=")[1])
    y = int(parts[1].split("=")[1])
    return x, y


def solve_equations(button_a, button_b, prize):
    a, b = sp.symbols("a b")
    eq1 = sp.Eq(button_a[0] * a + button_b[0] * b, prize[0])
    eq2 = sp.Eq(button_a[1] * a + button_b[1] * b, prize[1])
    solution = sp.solve((eq1, eq2), (a, b))
    return solution


# Part 1
def main1():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    used_tokens = 0

    # Parse the input and solve the equations for intersecting lines
    for i in range(0, len(lines), 4):
        button_a = parse_line(lines[i])
        button_b = parse_line(lines[i + 1])
        prize = parse_prize(lines[i + 2])

        solution = solve_equations(button_a, button_b, prize)
        if solution:
            a_val = solution[sp.symbols("a")]
            b_val = solution[sp.symbols("b")]
            # Find the minimum value of b if there are multiple solutions
            if isinstance(a_val, list) and isinstance(b_val, list):
                min_b_index = b_val.index(min(b_val))
                a_val = a_val[min_b_index]
                b_val = b_val[min_b_index]
            if a_val.is_integer and b_val.is_integer:
                used_tokens += a_val * 3 + b_val

    print(used_tokens)


# Part 2
def main2():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    used_tokens = 0

    # Parse the input and solve the equations for intersecting lines
    for i in range(0, len(lines), 4):
        button_a = parse_line(lines[i])
        button_b = parse_line(lines[i + 1])
        prize = parse_prize(lines[i + 2])
        prize = (prize[0] + 10_000_000_000_000, prize[1] + 10_000_000_000_000)

        solution = solve_equations(button_a, button_b, prize)
        if solution:
            a_val = solution[sp.symbols("a")]
            b_val = solution[sp.symbols("b")]
            # Find the minimum value of b if there are multiple solutions
            if isinstance(a_val, list) and isinstance(b_val, list):
                min_b_index = b_val.index(min(b_val))
                a_val = a_val[min_b_index]
                b_val = b_val[min_b_index]
            if a_val.is_integer and b_val.is_integer:
                used_tokens += a_val * 3 + b_val

    print(used_tokens)


if __name__ == "__main__":
    main1()
    main2()
