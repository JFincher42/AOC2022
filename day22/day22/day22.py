# AOC 2022 Day 22

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day22" / "day22"


def parse(instructions):
    inst = []
    num = ""
    for i in range(len(instructions)):
        if instructions[i].isdigit():
            num += instructions[i]
        else:
            inst.append((instructions[i], int(num)))
            num = ""

    inst.append(("", int(num)))
    return inst


def check_xy(x, y, board):
    return x < len(board[y]) and board[y][x] != " "


def move(x, y, d, board):
    if d == 0:  # Right
        x = (x + 1) % len(board[y])

    elif d == 1:  # Down
        y = (y + 1) % len(board)

    elif d == 2:  # Left
        x -= 1
        if x < 0:
            x = len(board[y]) - 1
        # x = (x + len(board[y])-1) % len(board[y])

    else:  # Up
        y = y - 1
        if y < 0:
            y = len(board) - 1
        # y = (y + len(board)-1) % len(board)

    return x, y


def get_face(x, y):
    if x >= 50 and x <= 99 and y >= 0 and y <= 49:
        return 0

    if x >= 100 and x <= 149 and y >= 0 and y <= 49:
        return 1

    if x >= 50 and x <= 99 and y >= 100 and y <= 149:
        return 2

    if x >= 0 and x <= 49 and y >= 100 and y <= 149:
        return 3

    if x >= 0 and x <= 49 and y >= 150 and y <= 199:
        return 4

    return 5


def get_next_face(face, d, x, y):

    if face == 0:
        # We'll never wrap right(0) or down(1)
        if d == 2:
            return (0, 0, y)
        elif d == 3:
            return (0, 0, 149 - x)

    if face == 1:
        # We'll never wrap left(2)
        if d == 0:
            return (2, 99, 149 - y)
        elif d == 1:
            return (2, 99, x - 50)
        elif d == 3:
            return (3, x - 100, 199)

    if face == 2:
        # we'll never wrap left(2) or up(3)
        if d == 0:
            return (2, 149, 149 - y)
        elif d == 1:
            return (2, 49, 100 + x)

    if face == 3:
        # We'll never wrap right(0) or down(1)
        if d == 2:
            return (0, 50, 149 - y)
        elif d == 3:
            return (0, 50, 50 + x)

    if face == 4:
        # We'll never wrap up(3)
        if d == 0:
            return (3, y - 100, 149)
        elif d == 1:
            return (1, 100 + x, 0)
        elif d == 2:
            return (1, 100 - y, 0)

    if face == 5:
        # We'll never wrap down(1)
        if d == 0:
            return (3, y + 50, 49)
        elif d == 2:
            return (1, y - 50, 100)

    return d, x, y


extents = {
    0: (50, 99, 0, 49),
    1: (100, 149, 0, 49),
    2: (50, 99, 100, 149),
    3: (0, 49, 100, 149),
    4: (0, 49, 150, 199),
    5: (50, 99, 50, 99),
}


def move_cube(x, y, d, board):

    # Which face are we on?
    face = get_face(x, y)

    # Now we need to move on this face
    # We need the face extents to figure out if we went over the edge
    minx, maxx, miny, maxy = extents[face]

    if d == 0:  # Right
        x += 1

    elif d == 1:  # Down
        y += 1

    elif d == 2:  # Left
        x -= 1

    else:  # Up
        y = y - 1

    if x > maxx or x < minx or y > maxy or y < miny:
        d, x, y = get_next_face(face, d, x, y)

    return x, y, d


def part1(lines):
    # Get the map and the instructions
    board = [line.rstrip() for line in lines[:-2]]
    instructions = parse(lines[-1])

    # Get the starting location
    curry = 0
    currx = board[0].index(".")

    # Right is 0, 1 is down, 2 is left, 3 is up
    currd = 0

    # Start processing instructions
    for inst in instructions:
        for _ in range(inst[1]):
            # Where do we move next
            newx, newy = move(currx, curry, currd, board)

            # Keep moving while we're in a bad spot
            while not check_xy(newx, newy, board):
                newx, newy = move(newx, newy, currd, board)

            # Now check if that move means we should stop
            if board[newy][newx] == "#":
                break

            # No stop, so we move to that new place
            currx, curry = newx, newy

        # Change direction
        if inst[0] == "R":
            currd = (currd + 1) % 4

        elif inst[0] == "L":
            currd = (currd + 3) % 4

    # Adjust the coordinates by 1, since we're zero based
    print(f"Final: X = {currx+1}, Y={curry+1}, Dir={currd}")
    return 1000 * (curry + 1) + 4 * (currx + 1) + currd


def part2(lines):
    board = [line.rstrip() for line in lines[:-2]]
    instructions = parse(lines[-1])

    # Get the starting location
    curry = 0
    currx = board[0].index(".")

    # Right is 0, 1 is down, 2 is left, 3 is up
    currd = 0

    # Start processing instructions
    for inst in instructions:
        for _ in range(inst[1]):
            # Where do we move next
            newx, newy, newd = move_cube(currx, curry, currd, board)

            # Keep moving while we're in a bad spot
            while not check_xy(newx, newy, board):
                newx, newy, newd = move_cube(newx, newy, newd, board)

            # Now check if that move means we should stop
            if board[newy][newx] == "#":
                break

            # No stop, so we move to that new place
            currx, curry, currd = newx, newy, newd

        # Change direction
        if inst[0] == "R":
            currd = (currd + 1) % 4

        elif inst[0] == "L":
            currd = (currd + 3) % 4

    # Adjust the coordinates by 1, since we're zero based
    print(f"Final: X = {currx+1}, Y={curry+1}, Dir={currd}")
    return 1000 * (curry + 1) + 4 * (currx + 1) + currd


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
