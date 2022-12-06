# AOC 2022 Day 06

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day06" / "day06"


def part1(lines):
    for line in lines:
        start = 0
        while start + 4 < len(line):
            if len(set(line[start:start + 4])) == 4:
                return start + 4
            start += 1


def part2(lines):
    for line in lines:
        start = 0
        while start + 14 < len(line):
            if len(set(line[start:start + 14])) == 14:
                return start + 14
            start += 1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
