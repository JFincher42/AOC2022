# AOC 2022 Day 24

import pathlib


root_path = pathlib.Path.home() / "git" / "AOC2022" / "day24" / "day24"


# Using this as a dataclass to hold the state in one thing
class State:
    def __init__(self, position, moves, blizzards):
        self.pos = position
        self.moves = moves
        self.blizzards = blizzards


def parse(lines):
    walls = set()
    blizzards = {"<": set(), ">": set(), "v": set(), "^": set()}

    # Figure out where all the walls and blizzards are
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                walls.add((x, y))
            elif lines[y][x] == ".":
                continue
            else:
                blizzards[lines[y][x]].add((x, y))

    return walls, blizzards


def move_blizzards(blizzards, walls, maxx, maxy):
    new_blizzards = {"<": set(), ">": set(), "v": set(), "^": set()}
    bdirs = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}

    # Look at each one
    for d in blizzards.keys():
        for bpos in blizzards[d]:
            newx = bpos[0] + bdirs[d][0]
            newy = bpos[1] + bdirs[d][1]

            # Did we move into a wall?
            if (newx, newy) in walls:
                if newx > maxx:
                    newx = 1
                if newx == 0:
                    newx = maxx
                if newy == 0:
                    newy = maxy - 1
                if newy >= maxy:
                    newy = 1

            new_blizzards[d].add((newx, newy))

    return new_blizzards


def draw(walls, blizzards, pos, finish):
    for y in range(finish[1] + 1):
        for x in range(finish[0] + 2):
            ch = "."
            b = 0

            if (x, y) in blizzards["<"]:
                b += 1
                ch = "<"
            if (x, y) in blizzards[">"]:
                b += 1
                ch = ">"
            if (x, y) in blizzards["v"]:
                b += 1
                ch = "v"
            if (x, y) in blizzards["^"]:
                b += 1
                ch = "^"

            if (x, y) in walls:
                ch = "#"
            if (x, y) == pos:
                ch = "E"

            if b > 1:
                print(b, end="")
            else:
                print(ch, end="")
        print()

    print()


def part1(lines, start, finish):
    # Here's the thinking -- we do a BFS through the valley
    # Using BFS was a hint from Reddit, but the rest of this is mine
    #
    # First state is our start position, zero moves, original blizzards
    #
    # We check for two things:
    # - Are we in teh same place as a blizzard?
    #   - If so, this is a bad move
    # - Are we at the end?
    #   - If so, we return the number of moves we made
    #
    # If neither are true, we check for the following moves:
    # - up,
    # - down,
    # - left,
    # - right,
    # - and wait (important)
    #
    # Each state we push consists of:
    # - The position we move to
    # - How many moves this will be
    # - The new positions of the blizzards
    #
    # Otherwise, standard BFS

    walls, blizzards = parse(lines)

    next_loc = [State(start, 0, blizzards)]

    draw(walls, blizzards, start, finish)

    visited = set()

    while len(next_loc) > 0:
        current_loc = next_loc.pop(0)

        # Get the blizzards
        blizzards = current_loc.blizzards

        # Get the current minute
        moves = current_loc.moves

        # Have we been here at this time before?
        if (current_loc.pos[0], current_loc.pos[1], current_loc.moves) in visited:
            continue
        else:
            visited.add((current_loc.pos[0], current_loc.pos[1], current_loc.moves))

        # Are we in the same place as a blizzard?
        for _, blocs in blizzards.items():
            if current_loc.pos in blocs:
                # This is an invalid position, we can't be here
                continue

        # Are we in a wall (shouldn't happen)
        if current_loc.pos in walls:
            continue

        # Are we at the end?
        if current_loc.pos == finish:
            draw(walls, blizzards, current_loc.pos, finish)

            # How many moves to get here
            return moves+1

        # Otherwise, we need to check all five moves
        # First, let's move all the blizzards
        blizzards = move_blizzards(blizzards, walls, finish[0], finish[1])

        # Let's draw everything
        # draw(walls, blizzards, current_loc.pos, finish)

        # Now let's add our five new moves
        # Move right
        newx, newy = current_loc.pos[0] + 1, current_loc.pos[1]
        if newx <= finish[0] and (newx, newy) not in walls:
            next_loc.append(
                State(
                    (newx, newy),
                    moves + 1,
                    blizzards,
                )
            )


        # Move down
        newx, newy = current_loc.pos[0], current_loc.pos[1] + 1
        if newy <= finish[1] and (newx, newy) not in walls:
            next_loc.append(
                State(
                    (newx, newy),
                    moves + 1,
                    blizzards,
                )
            )


        # Move left
        newx, newy = current_loc.pos[0] - 1, current_loc.pos[1]
        if newx > 0 and (newx, newy) not in walls:
            next_loc.append(
                State(
                    (newx, newy),
                    moves + 1,
                    blizzards,
                )
            )


        # Move up
        newx, newy = current_loc.pos[0], current_loc.pos[1] - 1
        if newy > 0 and (newx, newy) not in walls:
            next_loc.append(
                State(
                    (newx, newy),
                    moves + 1,
                    blizzards,
                )
            )

        # Wait
        next_loc.append(
            State(
                current_loc.pos,
                moves + 1,
                blizzards,
            )
        )


def part2(lines):
    pass


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines, (1,0), (100, 36))}")
    # print(f"Part 1: Answer: {part1(lines, (1,0), (6, 5))}")
    print(f"Part 2: Answer: {part2(lines)}")
