# AOC 2022 Day 18

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day18" / "day18"


def part1(lines):
    sides = 0

    droplet = set()

    for line in lines:
        x, y, z = line.split(",")
        x = int(x)
        y = int(y)
        z = int(z)

        sides += 6

        # Check if there is a cube on the other sides
        if (x + 1, y, z) in droplet:
            sides -= 2
        if (x - 1, y, z) in droplet:
            sides -= 2
        if (x, y + 1, z) in droplet:
            sides -= 2
        if (x, y - 1, z) in droplet:
            sides -= 2
        if (x, y, z + 1) in droplet:
            sides -= 2
        if (x, y, z - 1) in droplet:
            sides -= 2

        droplet.add((x, y, z))

    return sides


def part2(lines):
    sides = 0

    max_x, max_y, max_z = 0, 0, 0
    min_x, min_y, min_z = 20, 20, 20

    droplet = set()

    for line in lines:
        x, y, z = line.split(",")
        x = int(x)
        y = int(y)
        z = int(z)

        max_x = max(max_x, x)
        min_x = min(min_x, x)

        max_y = max(max_y, y)
        min_y = min(min_y, y)

        max_z = max(max_z, z)
        min_z = min(min_z, z)

        sides += 6

        # Check if there is a cube on the other sides
        if (x + 1, y, z) in droplet:
            sides -= 2
        if (x - 1, y, z) in droplet:
            sides -= 2
        if (x, y + 1, z) in droplet:
            sides -= 2
        if (x, y - 1, z) in droplet:
            sides -= 2
        if (x, y, z + 1) in droplet:
            sides -= 2
        if (x, y, z - 1) in droplet:
            sides -= 2

        droplet.add((x, y, z))

    # With some help from Reddit
    # Let's figure out all the air around the pellet
    # We can then check every point in the pellet
    # Check each side to see if it's adjacent to ghe surrounding air
    # If so, we we add that face

    # So how do we find all the surrounding air?
    # - Pick one of the air points
    # - Do a BFS to find every connected air point
    #   - Bound this by (min - 1, max + 1)
    #   - Also avoid already visited and lava points
    # - Store them all in another set

    # The first point can be (min_x, min_y, min_z)
    # But first we adjust the bounding box so there is connection
    min_x -= 1
    min_y -= 1
    min_z -= 1

    max_x += 1
    max_y += 1
    max_z += 1

    visited = set()

    queue = [(min_x, min_y, min_z)]

    while len(queue) > 0:
        point = queue.pop(0)
        visited.add(point)

        # Figure out which if the six adjacent points to add
        x, y, z = point
        if (
            x - 1 >= min_x
            and (x - 1, y, z) not in visited
            and (x - 1, y, z) not in droplet
        ):
            queue.append((x - 1, y, z))
            visited.add((x - 1, y, z))

        if (
            x + 1 <= max_x
            and (x + 1, y, z) not in visited
            and (x + 1, y, z) not in droplet
        ):
            queue.append((x + 1, y, z))
            visited.add((x + 1, y, z))

        if (
            y - 1 >= min_y
            and (x, y - 1, z) not in visited
            and (x, y - 1, z) not in droplet
        ):
            queue.append((x, y - 1, z))
            visited.add((x, y - 1, z))

        if (
            y + 1 <= max_y
            and (x, y + 1, z) not in visited
            and (x, y + 1, z) not in droplet
        ):
            queue.append((x, y + 1, z))
            visited.add((x, y + 1, z))

        if (
            z - 1 >= min_z
            and (x, y, z - 1) not in visited
            and (x, y, z - 1) not in droplet
        ):
            queue.append((x, y, z - 1))
            visited.add((x, y, z - 1))

        if (
            z + 1 <= max_z
            and (x, y, z + 1) not in visited
            and (x, y, z + 1) not in droplet
        ):
            queue.append((x, y, z + 1))
            visited.add((x, y, z + 1))

    # visited has all the connect air points, so we can go through the droplet points now
    faces = 0
    for droplet_point in droplet:
        x, y, z = droplet_point
        if (x - 1, y, z) in visited:
            faces += 1
        if (x + 1, y, z) in visited:
            faces += 1
        if (x, y - 1, z) in visited:
            faces += 1
        if (x, y + 1, z) in visited:
            faces += 1
        if (x, y, z - 1) in visited:
            faces += 1
        if (x, y, z + 1) in visited:
            faces += 1

    return faces


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
