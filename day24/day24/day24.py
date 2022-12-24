# AOC 2022 Day 24

import pathlib
from collections import deque


root_path = pathlib.Path.home() / "git" / "AOC2022" / "day24" / "day24"


def parse(lines):
    blizzards = {"<": set(), ">": set(), "v": set(), "^": set()}

    # Figure out where all the blizzards are
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] in "<>^v":
                # We subtract 1 to get to a zero based indexing
                blizzards[lines[y][x]].add((x - 1, y - 1))

    return blizzards


def in_blizzard(x, y, mx, my, t, blizzards):

    # We can use some math here 
    # Each blizzard moves in a straight line, one move per second
    # Which means after t seconds, it's moved t spaces
    # Which is the same as us moving t spaces the other way
    #
    # So if we check our position after moving t spaces in some direction
    # We can see if a blizzard moving the opposite way is there
    # If so, we can't be there.
    # 
    # This was taken from a Reddit post, but entered by hand and understood

    return any(
        (
            (x, (y - t) % my) in blizzards["v"],
            (x, (y + t) % my) in blizzards["^"],
            ((x - t) % mx, y) in blizzards[">"],
            ((x + t) % mx, y) in blizzards["<"],
        )
    )


def part1(lines, start, finish):
    # Here's the thinking -- we do a BFS through the valley
    # Using BFS was a hint from Reddit, but the rest of this is mine
    #
    # First state is our start position and the minutes
    # We can save this as a tuple
    #
    # We check for two things:
    # - Are we in teh same place as a blizzard?
    #   - If so, this is a bad move
    # - Are we at the end?
    #   - If so, we return the number of moves we made
    #
    # If neither are true, we check if the following moves are valid:
    # - up,
    # - down,
    # - left,
    # - right,
    # - and wait (important)
    #
    # Each state we push consists of:
    # - The position we move to
    # - How many moves this will be
    #
    # Otherwise, standard BFS

    # Get the blizzard positions
    blizzards = parse(lines)

    # Setup the queue
    next_loc = deque()

    # Keep trying to add a start position -- we may have to wait to enter
    time = 1
    while not next_loc:
        if not in_blizzard(start[0], start[1], finish[0], finish[1], time, blizzards):
            next_loc.append((start[0], start[1], time))
        else:
            time += 1

    visited = set()

    while len(next_loc) > 0:
        currx, curry, time = next_loc.popleft()

        # Have we been here at this time before?
        if (currx, curry, time) in visited:
            continue
        else:
            visited.add((currx, curry, time))

        # Are we in the same place as a blizzard?
        if in_blizzard(currx, curry, finish[0], finish[1], time, blizzards):
            # This won't work
            continue

        # Are we in a wall (shouldn't happen)
        # if (currx, curry) in walls:
        #     continue

        # Are we at the end?
        if (currx, curry) == (finish[0]-1, finish[1]-1):
            # draw(walls, blizzards, (currx, curry), finish)

            # How many moves to get here
            return time + 1

        # Now let's add our five new moves
        # Move right
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

        for dx, dy in moves:
            newx, newy = currx + dx, curry + dy
            if (
                0 <= newx < finish[0]
                and 0 <= newy < finish[1]
                and not in_blizzard(
                    newx, newy, finish[0], finish[1], time + 1, blizzards
                )
            ):
                next_loc.append((newx, newy, time + 1))


def part2(lines):
    pass


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines, (0,0), (100, 35))}")
    # print(f"Part 1: Answer: {part1(lines, (0,0), (6, 4))}")
    print(f"Part 2: Answer: {part2(lines)}")
