# AOC 2022 Day 08

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day08" / "day08"


def check_left(row, col, lines):
    height = int(lines[row][col])
    col -= 1
    while col >= 0:
        if int(lines[row][col]) >= height:
            return False
        col -= 1
    return True


def check_right(row, col, lines):
    height = int(lines[row][col])
    col += 1
    while col < len(lines[row]):
        if int(lines[row][col]) >= height:
            return False
        col += 1
    return True


def check_up(row, col, lines):
    height = int(lines[row][col])
    row -= 1
    while row >= 0:
        if int(lines[row][col]) >= height:
            return False
        row -= 1
    return True


def check_down(row, col, lines):
    height = int(lines[row][col])
    row += 1
    while row < len(lines):
        if int(lines[row][col]) >= height:
            return False
        row += 1
    return True


def count_left(row, col, lines):
    height = int(lines[row][col])
    col -= 1
    trees = 0
    while col >= 0:
        if int(lines[row][col]) >= height:
            return trees + 1
        trees += 1
        col -= 1
    return trees


def count_right(row, col, lines):
    height = int(lines[row][col])
    col += 1
    trees = 0
    while col < len(lines[row]):
        if int(lines[row][col]) >= height:
            return trees + 1
        trees += 1
        col += 1
    return trees


def count_up(row, col, lines):
    height = int(lines[row][col])
    row -= 1
    trees = 0
    while row >= 0:
        if int(lines[row][col]) >= height:
            return trees + 1
        trees += 1
        row -= 1
    return trees


def count_down(row, col, lines):
    height = int(lines[row][col])
    row += 1
    trees = 0
    while row < len(lines):
        if int(lines[row][col]) >= height:
            return trees + 1
        trees += 1
        row += 1
    return trees


def part1(lines):
    visible = 0
    for linecount in range(len(lines)):
        line = lines[linecount]
        for colcount in range(len(line)):
            if (
                linecount == 0
                or colcount == 0
                or linecount == len(lines) - 1
                or colcount == len(line) - 1
            ):
                visible += 1
            elif (
                check_left(linecount, colcount, lines)
                or check_right(linecount, colcount, lines)
                or check_up(linecount, colcount, lines)
                or check_down(linecount, colcount, lines)
            ):
                visible += 1

    return visible


def part2(lines):
    highscore = 0
    for linecount in range(len(lines)):
        line = lines[linecount]
        for colcount in range(len(line)):
            if (
                linecount == 0
                or colcount == 0
                or linecount == len(lines) - 1
                or colcount == len(line) - 1
            ):
                continue
            else:
                score = (
                    count_left(linecount, colcount, lines)
                    * count_right(linecount, colcount, lines)
                    * count_up(linecount, colcount, lines)
                    * count_down(linecount, colcount, lines)
                )
                highscore = max(highscore, score)

    return highscore


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
