import pathlib


def part1(data):
    count = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count


def window(data):

    return [data[i - 1] + data[i] + data[i + 1] for i in range(1, len(data) - 1)]


if __name__ == "__main__":

    lines = pathlib.Path('day1_data.txt').read_text().rstrip().split('\n')
    puzzle_input = [int(line) for line in lines]

    p1 = part1(puzzle_input)
    print(p1)

    w = window(puzzle_input)
    p2 = part1(w)
    print(p2)
