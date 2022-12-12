# AOC 2022 Day 01

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day01" / "day01"




def part1(lines):

    totals = []
    current_total = 0
    for line in lines:
        # If it's a blank line, check if we're a new max
        if line == "":
            totals.append(current_total)
            current_total=0
        
        else:
            # It's a number - convert it an add it
            current_total += int(line)

    # totals.sort(reverse=True)
    # return totals[0]
    return max(totals)

def part2(lines):

    totals = []
    current_total = 0
    for line in lines:
        # If it's a blank line, check if we're a new max
        if line == "":
            totals.append(current_total)
            current_total=0
        
        else:
            # It's a number - convert it an add it
            current_total += int(line)

    totals.sort(reverse=True)
    return totals[0]+totals[1]+totals[2]


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
