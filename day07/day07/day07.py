# AOC 2022 Day 07

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day07" / "day07"

current_line = 0

def parse(lines, tree=None):
    global current_line

    while current_line < len(lines):
        # Split the line so we can parse it
        line = lines[current_line].split()

        # What kind of line is it?
        # Are we changing into a folder
        if line[1] == "cd":
            # Do we backup?
            if line[2] == "..":
                current_line += 1
                return tree

            # Parse this folder
            current_line+=1
            if line[2] not in tree.keys():
                tree[line[2]]={}
            tree[line[2]] = parse(lines, tree[line[2]])

            # Do we have a tree yet?
            # if tree:
            #     current_line+=1
            #     tree[line[2]] = parse(lines, tree[line[2]])
            # else:
            #     tree = {line[2]: {}}
            #     current_line += 1

        # Are we listing files and folders?
        elif line[1] == "ls":
            current_line += 1

        # Otherwise, it's a file/folder
        else:
            # File or folder?
            if line[0] == "dir":
                tree[line[1]] = {}
            else:
                tree[line[1]] = int(line[0])
            current_line+=1
    return tree


def part1(lines):
    tree = parse(lines, {})
    

def part2(lines):
    pass

if __name__ == "__main__":

    # with open(root_path / "input", "r") as f:
    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
