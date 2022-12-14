# AOC 2022 Day 04

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day13" / "day13"


def compare_packets(left, right):
    # Keep checking until someone runs out
    value_count = max(len(left), len(right))

    for i in range(value_count):
        # Did the left run out of numbers? That's good
        if i >= len(left):
            return 1

        # Did the right run out of numbers? That's bad
        if i >= len(right):
            return -1

        # Get each value
        left_value = left[i]
        right_value = right[i]

        # Figure out how to compare them
        if isinstance(left_value, int) and isinstance(right_value, int):
            # Both integers, check if left < right
            if left_value < right_value:
                return 1
            elif left_value > right_value:
                return -1
            else:
                # They're the same, so continue
                continue

        # At this point, at least one of them is a list, so convert the other one
        if isinstance(left_value, int):
            left_value = [left_value]
        elif isinstance(right_value, int):
            right_value = [right_value]

        # They're both lists, so we do this again
        subpackets=compare_packets(left_value, right_value)
        if subpackets==0:
            continue
        else:
            return subpackets

    # If we're here, they were the same, so return 0
    return 0


def part1(lines):
    current_line = 0
    current_pair = 1
    correct_pairs = 0

    while current_line < len(lines):
        left = eval(lines[current_line])
        right = eval(lines[current_line + 1])
        if compare_packets(left, right) == 1:
            correct_pairs += current_pair
        current_line += 3
        current_pair += 1

    return correct_pairs


def part2(lines):
    current_line = 0
    correct_order_2 = 1
    correct_order_6 = 2

    while current_line < len(lines):
        if lines[current_line]=="":
            current_line += 1
            continue

        left = eval(lines[current_line])
        right = [2]
        if compare_packets(left, right) == 1:
            correct_order_2 += 1

        right = [6]
        if compare_packets(left, right) == 1:
            correct_order_6 += 1

        current_line += 1

    return correct_order_2 * correct_order_6


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
