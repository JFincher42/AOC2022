# AOC 2022 Day 25

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day25" / "day25"

digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
rev_digits = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
snafu_digits = {0: "00", 1: "01", 2: "02", 3: "1=", 4: "1-"}


def snafu_to_decimal(snafu):
    num = 0

    for ch in snafu:
        num *= 5
        num += digits[ch]

    return num


def snafu_add(num1, num2):
    result = ""
    rem = 0
    for x in range(len(num1)):
        sum = digits[num1[len(num1) - 1 - x]] + digits[num2[len(num2) - 1 - x]] + rem
        if sum > 2:
            rem = sum - 2
            sum -= 5
        else:
            rem = 0

        result = rev_digits[sum] + result

    if rem:
        result = rev_digits[rem] + result

    return result


def decimal_to_snafu(num):
    snafu = []
    while num > 5:
        snafu.append(snafu_digits[num % 5])
        num //= 5

    snafu.append(snafu_digits[num])

    # Make everything long enough to add
    # Pad each number out with zeros according to it's position and length
    # Remember there's in reverse order of where they should be

    pad_to = len(snafu) + 1
    zeroes = "0" * pad_to

    for x in range(len(snafu)):
        snafu[x] = zeroes[0 : pad_to - x] + snafu[x] + zeroes[0:x]

    # Now we can add all the numbers
    snafu_total = snafu[0]
    for addend in snafu[1:]:
        snafu_total = snafu_add(snafu_total, addend)

    return snafu_total


def part1(lines):
    total = 0
    for snafu in lines:
        total += snafu_to_decimal(snafu)

    return decimal_to_snafu(total)


def part2(lines):
    pass


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
    # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    # print(f"Part 2: Answer: {part2(lines)}")
