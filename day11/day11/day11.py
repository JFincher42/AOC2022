# AOC 2022 Day 11

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day11" / "day11"


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ""
        self.operand = ""
        self.divide = 0
        self.true_monkey = 0
        self.false_monkey = 0
        self.inspected = 0


def parse(lines):

    monkeys = []
    current_line = 0
    while current_line < len(lines):
        # First line is the monkey number
        current_monkey = Monkey()
        current_line += 1

        # Second line is the starting items
        items = lines[current_line][16:].strip().split(",")
        for item in items:
            current_monkey.items.append(int(item))
        current_line += 1

        # Third line is the operation and operand
        current_monkey.operation = lines[current_line][21]
        current_monkey.operand = lines[current_line][22:].strip()
        current_line += 1

        # Fourth line is the test
        current_monkey.divide = int(lines[current_line][19:])
        current_line += 1

        # Fifth is the true test
        current_monkey.true_monkey = int(lines[current_line][25])
        current_line += 1

        # Sixth is the false test
        current_monkey.false_monkey = int(lines[current_line][26])
        current_line += 1

        # Blank line to separate
        current_line += 1

        # Append this monkey
        monkeys.append(current_monkey)

    return monkeys


def calc_worry(worry, operator, operand, relief=3):
    if operand == "old":
        worry *= worry
    else:
        if operator == "+":
            worry += int(operand)
        else:
            worry *= int(operand)

    return worry // relief


def part1(lines):
    monkeys = parse(lines)
    for round in range(20):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                # Get the first item from the list
                item = monkey.items.pop(0)
                item = calc_worry(item, monkey.operation, monkey.operand)
                if item % monkey.divide == 0:
                    monkeys[monkey.true_monkey].items.append(item)
                else:
                    monkeys[monkey.false_monkey].items.append(item)

                monkey.inspected += 1

    monkey1 = 0
    monkey2 = 0
    for monkey in monkeys:
        if monkey.inspected > monkey1:
            monkey2 = monkey1
            monkey1 = monkey.inspected
        elif monkey.inspected > monkey2:
            monkey2 = monkey.inspected

    return monkey1 * monkey2


def part2(lines):
    monkeys = parse(lines)

    # Figure out the modulo constant to use to reduce worry later
    relief_mod = 1
    for monkey in monkeys:
        relief_mod *= monkey.divide

    # Run the simulation
    for round in range(10000):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                # Get the first item from the list
                item = monkey.items.pop(0)
                item = calc_worry(item, monkey.operation, monkey.operand, relief=1)
                item = item % relief_mod
                if item % monkey.divide == 0:
                    monkeys[monkey.true_monkey].items.append(item)
                else:
                    monkeys[monkey.false_monkey].items.append(item)

                monkey.inspected += 1

    monkey1 = 0
    monkey2 = 0
    for monkey in monkeys:
        if monkey.inspected > monkey1:
            monkey2 = monkey1
            monkey1 = monkey.inspected
        elif monkey.inspected > monkey2:
            monkey2 = monkey.inspected

    return monkey1 * monkey2


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
