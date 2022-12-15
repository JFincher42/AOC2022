# AOC 2022 Day 12

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day12" / "day12"


def find(lines, tile):
    for y in range(len(lines)):
        if tile in lines[y]:
            return lines[y].index(tile), y

def get_height(ch):
    if ch == "S":
        return ord('a')
    elif ch == "E":
        return ord('z')
    else:
        return ord(ch)

def get_next_tiles(lines, currx, curry):

    next_tiles = []
    height = get_height(lines[curry][currx])

    # Check if we're at the top or bottom
    if curry > 0:
        if get_height(lines[curry - 1][currx]) - height <= 1:
            next_tiles.append((currx, curry - 1))
    if curry < len(lines) - 1:
        if get_height(lines[curry + 1][currx]) - height <= 1:
            next_tiles.append((currx, curry + 1))

    # Check if we're at the left or right
    if currx > 0:
        if get_height(lines[curry][currx - 1]) - height <= 1:
            next_tiles.append((currx - 1, curry))
    if currx < len(lines[curry]) - 1:
        if get_height(lines[curry][currx + 1]) - height <= 1:
            next_tiles.append((currx + 1, curry))

    return next_tiles


def find_path(lines, startx, starty, endx, endy):
    next_tiles = [(startx, starty, 0)]
    explored = {}

    while len(next_tiles) > 0:
        (currx, curry, count) = next_tiles.pop(0)
        if (currx, curry) == (endx, endy):
            return count

        successors = get_next_tiles(lines, currx, curry)
        for child in successors:
            if child not in explored or explored[child] > count + 1:
                explored[child] = count + 1
                next_tiles.append((child[0], child[1], count + 1))

    # We never found it, so we return -1
    return -1


def part1(lines):
    startx, starty = find(lines, "S")
    endx, endy = find(lines, "E")

    return find_path(lines, startx, starty, endx, endy)


def part2(lines):
    starting_points = []
    starting_points.append(find(lines, "S"))
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x]=='a':
                starting_points.append((x,y))

    shortest = -1
    endx, endy = find(lines, "E")

    for starting_point in starting_points:
        path_length = find_path(lines, starting_point[0], starting_point[1], endx, endy)
        if path_length > -1:
            if shortest == -1 or path_length < shortest:
                shortest = path_length

    return shortest

if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
