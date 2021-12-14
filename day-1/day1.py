import pathlib


def part1(data):
    count = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count


def window(data):
    l = list()
    # si i = 1: window = 1, 2, 3 // si i = 2, window = 2,3,4 etc
    for i in range(1, len(data) - 1):
        l.append(data[i - 1] + data[i] + data[i + 1])
    return l


if __name__ == "__main__":

    lines = pathlib.Path('day1_data.txt').read_text().rstrip().split('\n')
    puzzle_input = [int(line) for line in lines]

    print(p1 = part1(puzzle_input))

    w = window(puzzle_input)
    p2 = part1(w)
    print(p2)
