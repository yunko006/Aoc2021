import pathlib


def part1(data):
    most_common = ""
    least_common = ""

    for i in range(len(data[0])):
        if [sublist[i] for sublist in data].count('0') > 500:
            most_common += "0"
        else:
            most_common += '1'

    for i in range(len(data[0])):
        if [sublist[i] for sublist in data].count('0') < 500:
            least_common += "0"
        else:
            least_common += '1'

    most_common_binary_to_int = int(f"{most_common}", 2)

    least_common_binary_to_int = int(f'{least_common}', 2)

    print(most_common_binary_to_int * least_common_binary_to_int)


def part2(data):
    pass


if __name__ == "__main__":

    lines = pathlib.Path('input.txt').read_text().rstrip().split('\n')
    puzzle_input_as_list = [list(line) for line in lines]
    puzzle_input = [line for line in lines]

    part1(puzzle_input_as_list)
