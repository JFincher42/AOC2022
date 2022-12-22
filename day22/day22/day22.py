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
    pass


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        # with open(root_path / "sample", "r") as f:
        lines = [line for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
