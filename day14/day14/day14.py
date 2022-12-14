# AOC 2022 Day 04

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day14" / "day14"


def parse(lines):
    lowest_point = 0
    rocks = set()

    # First, parse our input
    for line in lines:
        newline = True
        for coordinate in line:
            point = tuple([int(x) for x in coordinate.split(",")])
            lowest_point = max(point[1], lowest_point)

            if newline:
                start = point
                newline = False
            else:
                # Same row
                if start[0] == point[0]:
                    first = min(start[1], point[1])
                    last = max(start[1], point[1])
                    for i in range(first, last + 1):
                        # if [start[0], i] not in rocks:
                        #     rocks.append([start[0], i])
                        rocks.add((start[0], i))

                # Same column
                else:
                    first = min(start[0], point[0])
                    last = max(start[0], point[0])
                    for i in range(first, last + 1):
                        # if [i, start[1]] not in rocks:
                        #     rocks.append([i, start[1]])
                        rocks.add((i, start[1]))

            start = point
    return rocks, lowest_point


def part1(lines):
    sand = set()

    rocks, lowest_point = parse(lines)

    # Now we can track sand
    while True:
        unit = (500, 0)
        while unit[1] < lowest_point:
            # Check down
            if (unit[0], unit[1] + 1) not in rocks and (
                unit[0],
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0], unit[1] + 1)

            # Check down and left
            elif (unit[0] - 1, unit[1] + 1) not in rocks and (
                unit[0] - 1,
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0] - 1, unit[1] + 1)

            # Check down and right
            elif (unit[0] + 1, unit[1] + 1) not in rocks and (
                unit[0] + 1,
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0] + 1, unit[1] + 1)

            # We're done with this one
            else:
                # sand.append(unit)
                sand.add(unit)
                break

        # If we get here, then we're past the bottom and we can stop
        if unit[1] >= lowest_point:
            break

    # Count how many sand particles there are
    return len(sand)


def part2(lines):
    sand = set()

    rocks, lowest_point = parse(lines)
    lowest_point += 1

    # Now we can track sand
    while (500, 0) not in sand:
        unit = (500, 0)

        while True:

            # First check if we're just above the floor
            if unit[1] == lowest_point:
                # Add the floor below us
                rocks.add((unit[0], unit[1]+1))
                rocks.add((unit[0]+1, unit[1]+1))
                rocks.add((unit[0]-1, unit[1]+1))

            # Check down
            if (unit[0], unit[1] + 1) not in rocks and (
                unit[0],
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0], unit[1] + 1)

            # Check down and left
            elif (unit[0] - 1, unit[1] + 1) not in rocks and (
                unit[0] - 1,
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0] - 1, unit[1] + 1)

            # Check down and right
            elif (unit[0] + 1, unit[1] + 1) not in rocks and (
                unit[0] + 1,
                unit[1] + 1,
            ) not in sand:
                unit = (unit[0] + 1, unit[1] + 1)

            # We're done with this one
            else:
                # sand.append(unit)
                sand.add(unit)
                break

        # If we get here, then we're past the bottom and we can stop
        # if unit[1] >= lowest_point:
        #     break

    # Count how many sand particles there are
    return len(sand)


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip().split(" -> ") for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
