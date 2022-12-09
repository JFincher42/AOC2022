# AOC 2022 Day 04

import pathlib
from math import ceil, copysign

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day09" / "day09"

head_directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
tail_directions = {(-1, 2): (-1, 1)}


def part1(lines):
    hx, hy = 0, 0
    tx, ty = 0, 0
    tail_pos = set()
    for (direction, count) in lines:
        count = int(count)

        # Add the tail position to the set
        # tail_pos.add((tx, ty))

        # Loop through the new head positions
        for p in range(count):
            hx += head_directions[direction][0]
            hy += head_directions[direction][1]

            # What is the new direction to move the tail
            tx_diff = hx - tx
            ty_diff = hy - ty

            # If we're more than 2 away, we need to move the tail
            if abs(tx_diff) == 2 or abs(ty_diff) == 2:
                tx += copysign(ceil(abs(tx_diff) / 2), tx_diff)
                ty += copysign(ceil(abs(ty_diff) / 2), ty_diff)

            # Add the new tail position
            tail_pos.add((tx, ty))

    # print(tail_pos)
    return len(tail_pos)


def part2(lines):
    # Ten knots instead of two
    # Head knot is 0, tail is 9
    knots = [[0, 0] for i in range(10)]

    tail_pos = set()
    for (direction, count) in lines:
        count = int(count)

        # Loop through the new head positions
        for p in range(count):
            knots[0][0] += head_directions[direction][0]
            knots[0][1] += head_directions[direction][1]

            # Now we figure out how each knot follows the one in front of it
            for knot in range(1, 10):
                diffx = knots[knot - 1][0] - knots[knot][0]
                diffy = knots[knot - 1][1] - knots[knot][1]

                if abs(diffx) == 2 or abs(diffy) == 2:
                    knots[knot][0] += copysign(ceil(abs(diffx) / 2), diffx)
                    knots[knot][1] += copysign(ceil(abs(diffy) / 2), diffy)

            # Add the tail knot position
            tail_pos.add((knots[9][0], knots[9][1]))

    return len(tail_pos)


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample2", "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
