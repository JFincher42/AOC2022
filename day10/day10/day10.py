# AOC 2022 Day 04

import pathlib
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day10" / "day10"


def part1(lines):
    x = 1
    cycle = 1
    strength = 0
    for line in lines:
        inst = line.split()
        if inst[0] == "noop":
            cycle += 1
        else:
            cycle += 2
            x += int(inst[1])

        if cycle in [20, 60, 100, 140, 180, 220]:
            strength += cycle * x
        elif cycle in [21, 61, 101, 141, 181, 221] and inst[0] == "addx":
            strength += (cycle - 1) * (x - int(inst[1]))

    return strength


def part2(lines):
    sprite = [0, 1, 2]
    crt = [[" " for i in range(40)] for j in range(6)]
    cycle = 0
    row, col = 0, 0
    for line in lines:
        inst = line.split()
        if inst[0] == "noop":
            # Draw the pixel
            if col in sprite:
                crt[row][col] = "#"
                
            # Next cycle
            cycle += 1

            # New CRT position
            row += (col + 1) // 40
            col = (col + 1) % 40


        else:
            # Draw the pixel
            if col in sprite:
                crt[row][col] = "#"

            # Next cycle
            cycle += 1

            # New CRT position
            row += (col + 1) // 40
            col = (col + 1) % 40


            # Second cycle
            # Draw the pixel
            if col in sprite:
                crt[row][col] = "#"

            # Update the sprite
            sprite[0] += int(inst[1])
            sprite[1] += int(inst[1])
            sprite[2] += int(inst[1])

            # Next cycle
            cycle += 1

            # New crt position
            row += (col + 1) // 40
            col = (col + 1) % 40


    for x in range(6):
        for y in range(40):
            print(crt[x][y], end="")
        print()


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
