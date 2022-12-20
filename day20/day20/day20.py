# AOC 2022 Day 20

import pathlib
from collections import deque
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day20" / "day20"


def print_mix(mix):
    for item in mix:
        print(f"{item}, ", end="")
    print()


def part1(sequence):
    # Create a deque which holds the number and it's place in the sequence

    mix = deque()
    for i in range(len(sequence)):
        mix.append((sequence[i], i))

    # print_mix(mix)
    # print(f"Mix is {len(mix)} numbers long")

    for i in range(len(sequence)):
        if sequence[i] != 0:
            # Rotate the number into position
            mix.rotate(mix.index((sequence[i], i)) * -1)

            # Pop it off the queue
            mix.popleft()

            # Rotate to a new position
            mix.rotate(sequence[i] * -1)

            # Push the number back on
            mix.appendleft((sequence[i], i))

            # Rotate it back
            mix.rotate(sequence[i])

        # print_mix(mix)

    # print_mix(mix)
    # print()

    # Now we find the 0 and put it in position

    zero_index = sequence.index(0)
    mix.rotate(mix.index((0, zero_index)) * -1)

    # Now we find the 1_000th, 2_000th, and 3_000th number after this
    coordinates = 0
    mix.rotate(-1000)
    coordinates += mix[0][0]
    mix.rotate(-1000)
    coordinates += mix[0][0]
    mix.rotate(-1000)
    coordinates += mix[0][0]

    return coordinates


def part2(sequence):
    # Create a deque which holds the number and it's place in the sequence

    mix = deque()
    for i in range(len(sequence)):
        sequence[i] *= 811589153
        mix.append((sequence[i], i))

    # print_mix(mix)
    # print(f"Mix is {len(mix)} numbers long")

    # Mix this up ten time

    for x in range(10):

        for i in range(len(sequence)):
            if sequence[i] != 0:
                # Rotate the number into position
                mix.rotate(mix.index((sequence[i], i)) * -1)

                # Pop it off the queue
                mix.popleft()

                # Rotate to a new position
                mix.rotate(sequence[i] * -1)

                # Push the number back on
                mix.appendleft((sequence[i], i))

                # Rotate it back
                mix.rotate(sequence[i])

    # Now we find the 0 and put it in position

    zero_index = sequence.index(0)
    mix.rotate(mix.index((0, zero_index)) * -1)

    # Now we find the 1_000th, 2_000th, and 3_000th number after this
    coordinates = 0
    mix.rotate(-1000)
    coordinates += mix[0][0]
    mix.rotate(-1000)
    coordinates += mix[0][0]
    mix.rotate(-1000)
    coordinates += mix[0][0]

    return coordinates


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [int(line) for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
