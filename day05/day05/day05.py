# AOC 2022 Day 05

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day05" / "day05"

def parse_move(line):
    spl = line.split(" ")
    return int(spl[1]), int(spl[3])-1, int(spl[5])-1

def part1(lines, stacks, move):
    while move < len(lines):
        (count, fr, to) = parse_move(lines[move])
        for i in range(count):
            stacks[to].append(stacks[fr].pop())
        move += 1

    retval = ""
    for i in range(len(stacks)):
        retval += stacks[i].pop()

    return retval


def part2(lines, stacks, move):
    while move < len(lines):
        (count, fr, to) = parse_move(lines[move])
        temp = []
        for i in range(count):
            temp.append(stacks[fr].pop())
        for i in range(count):
            stacks[to].append(temp.pop())
        move += 1

    retval = ""
    for i in range(len(stacks)):
        retval += stacks[i].pop()

    return retval

def parse(lines, bottom):
    stacks = [[] for x in range(bottom)]
    for line in range(bottom-1, -1, -1):
        crate = 0
        while crate*4+1 < len(lines[line]):
            if lines[line][crate*4+1].isupper():
                stacks[crate].append(lines[line][crate*4+1])
            crate += 1
    return stacks


if __name__ == "__main__":

    ###
    ### Sample Input
    # with open(root_path / "sample", "r") as f:
    #     lines = [line for line in f.readlines()]

    # stacks = parse(lines, 3)  # For the sample input
    # print(f"Part 1: Answer: {part1(lines, stacks, 5)}")

    # stacks = parse(lines, 3)  # For the sample input
    # print(f"Part 2: Answer: {part2(lines, stacks, 5)}")


    ###
    ### Real Input
    with open(root_path / "input", "r") as f:
        lines = [line for line in f.readlines()]

    stacks = parse(lines, 9)  # For the real input
    print(f"Part 1: Answer: {part1(lines, stacks, 10)}")

    stacks = parse(lines, 9)  # For the real input
    print(f"Part 2: Answer: {part2(lines, stacks, 10)}")
