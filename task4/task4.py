import sys


def count_moves(numbers):
    numbers.sort()
    average = numbers[len(numbers) // 2]

    moves = sum(abs(num - average) for num in numbers)
    return moves


# numbers_path = 'numbers.txt'
numbers_path = sys.argv[1]
nums = []

with open(numbers_path, 'r') as file:
    for line in file:
        el = int(line.strip())
        nums.append(el)

print(count_moves(nums))
