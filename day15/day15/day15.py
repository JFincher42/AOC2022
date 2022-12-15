# AOC 2022 Day 15

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day15" / "day15"


def parse(lines):
    sensors = []
    beacons = []

    for line in lines:
        parts = line.split(",")

        # First part is the sensor x, after an "="
        sensor_x = int(parts[0].split("=")[1])

        # Second part has both the sensor y and beacon x
        part1 = parts[1].split("=")
        sensor_y = int(part1[1].split(":")[0])
        beacon_x = int(part1[2])

        # Third part has beacon y
        beacon_y = int(parts[2].split("=")[1])

        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))

    return sensors, beacons


def part1(lines, row=2000000):
    sensors, beacons = parse(lines)
    row_cover = set()

    # Let's figure out the distance between each
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]

        # Distance is manhattan distance
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        # Figure out if we can cross the row we're concerned with
        # If the distance from the sensor to the row
        #    is less than the manhattan distance to the closest beacon
        #    we've got coverage
        row_dist = abs(sensor[1] - row)
        if row_dist <= dist:
            # Figure out how many items would be covered
            diff = dist - row_dist
            for cover_x in range(diff + 1):
                row_cover.add((sensor[0] + cover_x, row))
                row_cover.add((sensor[0] - cover_x, row))

        # Is this beacon covered on this row? We need to remove it
        if beacon in row_cover:
            row_cover.remove(beacon)

    return len(row_cover)


def in_scope(x, y, sensors, dists, max):
    if x > max or y > max or x < 0 or y < 0:
        return True

    in_range = False
    for i in range(len(sensors)):
        sensor = sensors[i]
        dist = dists[i]
        in_range = in_range or (abs(sensor[0] - x) + abs(sensor[1] - y) <= dist)

    return in_range


def part2(lines, max=4000000):
    sensors, beacons = parse(lines)

    # OK, general idea from Reddit:
    # - Locate each point just outside the range of each sensor
    # - Check if that point is in range of another sensor
    # - If so, check the next point
    # - If not, that's the point we need
    #

    # First, let's figure out the effective range of each sensor
    dists = []
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]

        # Distance is manhattan distance
        dists.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))

    # Now we can start looping over the sensors
    for i in range(len(sensors)):
        sensor = sensors[i]

        # Now we can figure out the perimeter of the sensor
        for x in range(dists[i] + 1):
            # We need to check four points
            # - sensor[0] + x, sensor[1] + (dist[i] - x)
            # - sensor[0] - x, sensor[1] + (dist[i] - x)
            # - sensor[0] + x, sensor[1] - (dist[i] - x)
            # - sensor[0] - x, sensor[1] - (dist[i] - x)

            perimeter_x1 = sensor[0] + x
            perimeter_x2 = sensor[0] - x
            perimeter_y1 = sensor[1] + (dists[i] + 1 - x)
            perimeter_y2 = sensor[1] - (dists[i] + 1 - x)

            # Check if this point is within the scope of another sensor
            if not in_scope(perimeter_x1, perimeter_y1, sensors, dists, max):
                # This must be our point
                print(f"Found ({perimeter_x1}, {perimeter_y1})")
                return perimeter_x1 * 4000000 + perimeter_y1

            # Not this one, check another
            if not in_scope(perimeter_x2, perimeter_y1, sensors, dists, max):
                # This must be our point
                print(f"Found ({perimeter_x2}, {perimeter_y1})")
                return perimeter_x2 * 4000000 + perimeter_y1

            # Not this one, check another
            if not in_scope(perimeter_x1, perimeter_y2, sensors, dists, max):
                # This must be our point
                print(f"Found ({perimeter_x1}, {perimeter_y2})")
                return perimeter_x1 * 4000000 + perimeter_y2

            # Not this one, check another
            if not in_scope(perimeter_x2, perimeter_y2, sensors, dists, max):
                # This must be our point
                print(f"Found ({perimeter_x2}, {perimeter_y2})")
                return perimeter_x2 * 4000000 + perimeter_y2

    return -1


if __name__ == "__main__":

    # with open(root_path / "sample", "r") as f:
    #     lines = [line.strip() for line in f.readlines()]

    # print(f"Part 1: Answer: {part1(lines, row=10)}")
    # print(f"Part 2: Answer: {part2(lines, max=20)}")

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
