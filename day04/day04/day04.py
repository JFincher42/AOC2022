# AOC 2022 Day 04

import pathlib
import string

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day04" / "day04"


def part1(lines):
    overlaps = 0
    for assignments in lines:
        assignment1 = [
            int(assignments[0].split("-")[0]),
            int(assignments[0].split("-")[1]),
        ]
        assignment2 = [
            int(assignments[1].split("-")[0]),
            int(assignments[1].split("-")[1]),
        ]

        if (
            (assignment1[0] <= assignment2[0]) and (assignment1[1] >= assignment2[1])
        ) or (
            (assignment2[0] <= assignment1[0]) and (assignment2[1] >= assignment1[1])
        ):
            overlaps += 1

    return overlaps


def part2(lines):
    overlaps = 0
    for assignments in lines:
        assignment1 = [
            int(assignments[0].split("-")[0]),
            int(assignments[0].split("-")[1]),
        ]
        assignment2 = [
            int(assignments[1].split("-")[0]),
            int(assignments[1].split("-")[1]),
        ]

        if (
            (assignment1[0] <= assignment2[0]) and (assignment1[1] >= assignment2[0])
        ) or (
            (assignment2[0] <= assignment1[0]) and (assignment2[1] >= assignment1[0])
        ):
            overlaps += 1

    return overlaps


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
