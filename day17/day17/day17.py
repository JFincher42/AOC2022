# AOC 2022 Day 17

import pathlib
from math import pow

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day17" / "day17"

rock1 = ["####"]
rock2 = [".#.", "###", ".#."]
rock3 = ["..#", "..#", "###"]
rock4 = ["#", "#", "#", "#"]
rock5 = ["##", "##"]

leftmost = [
    [(0, 0)],
    [(1, 0), (0, 1), (1, 2)],
    [(2, 0), (2, 1), (0, 2)],
    [(0, 3), (0, 2), (0, 1), (0, 0)],
    [(0, 1), (0, 0)],
]
rightmost = [
    [(3, 0)],
    [(1, 0), (2, 1), (1, 2)],
    [(2, 2), (2, 1), (2, 0)],
    [(0, 3), (0, 2), (0, 1), (0, 0)],
    [(1, 1), (1, 0)],
]
bottom = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 2), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 3)],
    [(0, 1), (1, 1)],
]

rocks = [rock1, rock2, rock3, rock4, rock5]


def check_lr(rock, rock_x, rock_y, chamber, move):
    # Check if we can even move left or right

    # Start with left
    if move == "<":
        moves = leftmost[rock]
        for move in moves:
            # is something blocking us from moving left?
            move_x = rock_x + move[0] - 1
            move_y = rock_y - move[1]

            if move_x < 0 or chamber[move_y][move_x] != ".":
                return 0

        return -1

    else:
        moves = rightmost[rock]
        for move in moves:
            # is something blocking us from moving left?
            move_x = rock_x + move[0] + 1
            move_y = rock_y - move[1]

            if move_x >= 7 or chamber[move_y][move_x] != ".":
                return 0

        return 1


def check_down(rock, rock_x, rock_y, chamber):
    # Check if we can even move down

    moves = bottom[rock]

    # We need to check every part of the bottom
    for move in moves:
        move_x = rock_x + move[0]
        move_y = rock_y - move[1] - 1

        if move_y < 0 or chamber[move_y][move_x] != ".":
            return False

    return True


def find_highest_rock(chamber):
    for i in range(len(chamber), 0, -1):
        if "@" in chamber[i - 1]:
            return i

    return 0


def part1(jets):
    current_rock = 0
    stopped_rocks = 0

    current_jet = 0

    chamber = [".......", ".......", ".......", "......."]
    highest_rock = 0

    while stopped_rocks < 2022:
        # First, position the upper left corner of the new rock
        rock_x = 2
        rock_y = highest_rock + 2 + len(rocks[current_rock])

        stopped = False

        # Start the rock movement
        while not stopped:
            # Which way do we move
            rock_x += check_lr(current_rock, rock_x, rock_y, chamber, jets[current_jet])

            # Next jet
            current_jet = (current_jet + 1) % len(jets)

            # Can we keep moving down
            if check_down(current_rock, rock_x, rock_y, chamber):
                rock_y -= 1
            else:
                # Commit this to the chamber
                for i in range(len(rocks[current_rock])):
                    rock_line = rocks[current_rock][i]
                    for j in range(len(rock_line)):
                        if rock_line[j] == "#":
                            chamber[rock_y - i] = (
                                chamber[rock_y - i][0 : rock_x + j]
                                + "@"
                                + chamber[rock_y - i][rock_x + j + 1 :]
                            )

                # Signal we're done with this rock
                stopped = True
                stopped_rocks += 1

        # Print the current chamber
        # for i in range(len(chamber), 0, -1):
        #     print(f"|{chamber[i-1]}|")
        # print("+-------+")
        # print
        # Next rock
        current_rock = (current_rock + 1) % 5

        # Find the highest rock, adjust the chamber
        highest_rock = find_highest_rock(chamber)
        lines_to_add = highest_rock + 3 + len(rocks[current_rock]) - len(chamber)
        for i in range(lines_to_add):
            chamber.append(".......")

    return find_highest_rock(chamber)


def convert(level):
    num = 0
    for i in range(len(level)):
        if level[i] == "@":
            num += pow(2, i)
    return num


def convert_chamber(chamber):
    num_chamber = []
    for i in range(len(chamber)):
        num = convert(chamber[i])
        if num != 0:
            num_chamber.append(num)
        else:
            break
    return num_chamber


def cycle_check(numbers):
    # Make sure there's enough for a cycle
    if len(numbers) < 3:
        return (0, 0)

    # Starting positions
    t = 1
    h = 2

    while numbers[t] != numbers[h]:
        t += 1
        h = t * 2
        if h >= len(numbers):
            return (0, 0)

    # We found a repeat here, let's find the start of pattern
    while numbers[t - 1] == numbers[h - 1]:
        t -= 1
        h -= 1

    # So now we have the start and the period
    return t, h - t + 1


def part2(jets):
    # Basically, we need to do the same thing as part 1, but with the following:
    # - When each rock stops, we need to check for a cycle
    # - Once we have the length of the cycle, we need to know how the height changes each cycle
    # - We do some math to figure out the height after 1_000_000_000_000 rocks
    # - We can then resume the count with the remainder, and add that to our calculation

    # For cycle checking, we can convert each line of the chamber into a number

    current_rock = 0
    stopped_rocks = 0

    current_jet = 0

    chamber = [".......", ".......", ".......", "......."]
    highest_rock = 0

    while True:
        # First, position the upper left corner of the new rock
        rock_x = 2
        rock_y = highest_rock + 2 + len(rocks[current_rock])

        stopped = False

        # Start the rock movement
        while not stopped:
            # Which way do we move
            rock_x += check_lr(current_rock, rock_x, rock_y, chamber, jets[current_jet])

            # Next jet
            current_jet = (current_jet + 1) % len(jets)

            # Can we keep moving down
            if check_down(current_rock, rock_x, rock_y, chamber):
                rock_y -= 1
            else:
                # Commit this to the chamber
                for i in range(len(rocks[current_rock])):
                    rock_line = rocks[current_rock][i]
                    for j in range(len(rock_line)):
                        if rock_line[j] == "#":
                            chamber[rock_y - i] = (
                                chamber[rock_y - i][0 : rock_x + j]
                                + "@"
                                + chamber[rock_y - i][rock_x + j + 1 :]
                            )

                # Signal we're done with this rock
                stopped = True
                stopped_rocks += 1

        # Check for a cycle now
        start, length = cycle_check(convert_chamber(chamber))
        if start > 0 and length > 0:
            # We found a cycle
            break

        current_rock = (current_rock + 1) % 5

        # Find the highest rock, adjust the chamber
        highest_rock = find_highest_rock(chamber)
        lines_to_add = highest_rock + 3 + len(rocks[current_rock]) - len(chamber)
        for i in range(lines_to_add):
            chamber.append(".......")

    print(f"Cycle found starting at {start}, length of {length}")

    # Print the current chamber
    for i in range(len(chamber), 0, -1):
        print(f"|{chamber[i-1]}|")
    print("+-------+")
    print


if __name__ == "__main__":

    # with open(root_path / "input", "r") as f:
    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines[0])}")
    print(f"Part 2: Answer: {part2(lines[0])}")
