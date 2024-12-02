def split_sides(p_input: str) -> tuple[list, list]:
    left = []
    right = []
    for line in p_input.splitlines():
        line_split = line.split()
        left.append(int(line_split[0]))
        right.append(int(line_split[1]))
    return left, right


def solve_part1(p_input: str) -> int:
    # split the sides
    left, right = split_sides(p_input)

    # sort to pair the smallest numbers
    left = sorted(left)
    right = sorted(right)

    # calculate total distance
    total_distance = sum(
        map(lambda x, y: abs(x-y), left, right)
    )
    return total_distance


def solve_part2(p_input: str) -> int:
    left, right = split_sides(p_input)

    return sum(
        map(lambda n: n * right.count(n), left)
    )

example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("inputs/day1.txt") as f:
    my_input = f.read()

assert solve_part1(example_input) == 11
assert solve_part2(example_input) == 31

print("Part 1:", solve_part1(my_input))
print("Part 2:", solve_part2(my_input))