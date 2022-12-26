# AOC 2022 Day 23

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day23" / "day23"


def parse(lines):
    ground = set()
    minx, maxx, miny, maxy = 0, 0, 0, 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                ground.add((x, y))
                minx = min(x, minx)
                maxx = max(x, maxx)
                miny = min(y, miny)
                maxy = max(y, maxy)
    return ground, minx, maxx, miny, maxy


def alone(elf, ground):
    neighbor = False
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            neighbor = neighbor or ((elf[0] + x, elf[1] + y) in ground)
    return neighbor


def north(elf, ground):
    neighbor = False
    for x in range(-1, 2):
        neighbor = neighbor or ((elf[0] + x, elf[1] - 1) in ground)
    return neighbor, 0, -1


def south(elf, ground):
    neighbor = False
    for x in range(-1, 2):
        neighbor = neighbor or ((elf[0] + x, elf[1] + 1) in ground)
    return neighbor, 0, 1


def west(elf, ground):
    neighbor = False
    for y in range(-1, 2):
        neighbor = neighbor or ((elf[0] - 1, elf[1] + y) in ground)
    return neighbor, -1, 0


def east(elf, ground):
    neighbor = False
    for y in range(-1, 2):
        neighbor = neighbor or ((elf[0] + 1, elf[1] + y) in ground)
    return neighbor, 1, 0


def part1(lines):
    ground, minx, maxx, miny, maxy = parse(lines)
    # print(f"Before: Elves = {len(ground)}, Min/Max = ({minx}, {miny})/({maxx},{maxy})")

    checks = [north, south, west, east]

    # Go for ten rounds
    for _ in range(10):
        # We need a place to store proposed moves
        # Store it as a dict, with the location to move as a key
        # And the elf who wants to move there as the value in a list
        # Any list with len > 1 is skipped.
        proposed = {}
        newground = set()

        # Check each elf each round
        for elf in ground:

            # Are we alone?
            if alone(elf, ground):

                # Check each direction
                for d in range(4):
                    check, x, y = checks[d](elf, ground)
                    if not check:
                        newelf = (elf[0] + x, elf[1] + y)
                        if newelf not in proposed.keys():
                            proposed[newelf] = []
                        proposed[newelf].append(elf)
                        # No need to check further
                        break

                # We couldn't move anywhere, so just add this elf
                if check:
                    newground.add(elf)

            # Here, we know we're alone, so just add this elf to the new ground
            else:
                newground.add(elf)

        # Here, we've processed all the elves this round
        # Let's see who can move

        for newelf, oldelf in proposed.items():
            if len(oldelf) == 1:
                newground.add(newelf)
                # Update the min and max
                minx = min(minx, newelf[0])
                maxx = max(maxx, newelf[0])
                miny = min(miny, newelf[1])
                maxy = max(maxy, newelf[1])
            else:
                # Just append the elves who couldn't move
                for elf in oldelf:
                    newground.add(elf)

        # We have new ground, so replace it
        ground = newground

        # Now we can rotate the direction
        checks.append(checks[0])
        checks = checks[1:]

    # Let's figure out the empty spaces

    # print(f"After: Elves = {len(ground)}, Min/Max = ({minx}, {miny})/({maxx},{maxy})")

    width = maxx - minx + 1
    height = maxy - miny + 1
    return (width * height) - len(ground)


def part2(lines):
    ground, minx, maxx, miny, maxy = parse(lines)

    checks = [north, south, west, east]

    # Go until we stop moving
    moved = True
    round = 0
    while moved:
        # We need a place to store proposed moves
        # Store it as a dict, with the location to move as a key
        # And the elf who wants to move there as the value in a list
        # Any list with len > 1 is skipped.
        proposed = {}
        newground = set()

        # Assume we haven't moved at all
        moved = False

        # New round
        round += 1

        # Check each elf each round
        for elf in ground:

            # Are we alone?
            if alone(elf, ground):

                # Check each direction
                for d in range(4):
                    check, x, y = checks[d](elf, ground)
                    if not check:
                        newelf = (elf[0] + x, elf[1] + y)
                        if newelf not in proposed.keys():
                            proposed[newelf] = []
                        proposed[newelf].append(elf)
                        # No need to check further
                        break

                # We couldn't move anywhere, so just add this elf
                if check:
                    newground.add(elf)

            # Here, we know we're alone, so just add this elf to the new ground
            else:
                newground.add(elf)

        # Here, we've processed all the elves this round
        # Let's see who can move

        for newelf, oldelf in proposed.items():
            if len(oldelf) == 1:
                newground.add(newelf)
                # Update the min and max
                minx = min(minx, newelf[0])
                maxx = max(maxx, newelf[0])
                miny = min(miny, newelf[1])
                maxy = max(maxy, newelf[1])
                # We've moved an elf, so indicate that
                moved = True
            else:
                # Just append the elves who couldn't move
                for elf in oldelf:
                    newground.add(elf)

        # We have new ground, so replace it
        ground = newground

        # Now we can rotate the direction
        checks.append(checks[0])
        checks = checks[1:]

    # How many rounds did we do?
    return round


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
