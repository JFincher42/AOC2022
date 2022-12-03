# AOC 2022 Day 03

import pathlib
import string

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day03" / "day03"


def part1(lines):
    priority = 0
    for line in lines:
        first = line[: len(line) // 2]
        last = line[len(line) // 2 :]
        for ch in first:
            if ch in last:
                priority += string.ascii_letters.index(ch)+1
                break

    return priority


def part2(lines):

    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
