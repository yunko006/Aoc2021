import pathlib


def part1(data):
    horizontal = 0
    depth = 0

    for i in range(len(data)):
        if "forward" in data[i]:
            horizontal += int(data[i][-1])
        elif "down" in data[i]:
            depth += int(data[i][-1])
        elif "up" in data[i]:
            depth -= int(data[i][-1])

    print(horizontal * depth)


def part2(data):
    aim = 0
    horizontal = 0
    depth = 0

    for i in range(len(data)):
        if "forward" in data[i]:
            horizontal += int(data[i][-1])
            if aim:
                depth += aim * int(data[i][-1])
        elif "down" in data[i]:
            aim += int(data[i][-1])
        elif "up" in data[i]:
            aim -= int(data[i][-1])

    print(horizontal * depth)


if __name__ == "__main__":

    lines = pathlib.Path('input.txt').read_text().rstrip().split('\n')
    puzzle_input = [line for line in lines]

    # print("forward" in puzzle_input[0])
    # print(puzzle_input[0][-1])

    # part1(puzzle_input)
    part2(puzzle_input)
