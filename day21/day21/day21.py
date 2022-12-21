# AOC 2022 Day 21

import pathlib
from copy import deepcopy

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day21" / "day21"


def get_value(monkeys, which):
    # Does this monkey have a number?
    if not isinstance(monkeys[which], str):
        return monkeys[which]

    # Not a number so figure out which two monkeys values to get
    op1 = monkeys[which][0:4]
    op2 = monkeys[which][7:]

    # Get the operator as well
    operator = monkeys[which][5]

    # Get and store the values for each
    val1 = get_value(monkeys, op1)
    monkeys[op1] = val1
    val2 = get_value(monkeys, op2)
    monkeys[op2] = val2

    # Figure out this value and store it
    value = eval(f"int({val1}{operator}{val2})")
    monkeys[which] = value

    # And return it
    return value


def part1(lines):
    monkeys = {}
    for line in lines:
        monkey = line.split(":")
        if len(monkey[1]) < 8:
            monkeys[monkey[0]] = int(monkey[1].strip())
        else:
            monkeys[monkey[0]] = monkey[1].strip()

    return get_value(monkeys, "root")


def part2(lines):
    monkeys = {}
    for line in lines:
        monkey = line.split(":")
        if len(monkey[1]) < 8:
            monkeys[monkey[0]] = int(monkey[1].strip())
        else:
            monkeys[monkey[0]] = monkey[1].strip()

    # Start a loop

    humn = 3093175982595

    while True:
        # print(f"Trying HUMN = {humn}...")
        monkey_copy = deepcopy(monkeys)
        monkey_copy["humn"] = humn

        # Get the two halves of root
        op1 = monkey_copy["root"][0:4]
        op2 = monkey_copy["root"][7:]

        val1 = get_value(monkey_copy, op1)
        monkey_copy[op1] = val1
        val2 = get_value(monkey_copy, op2)
        monkey_copy[op2] = val2

        # print(f"HUMN= {humn}, diff = {val1-val2}")

        # Are they equal
        if val1 == val2:
            break

        # Nope, next number
        humn += 3

    return humn


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
