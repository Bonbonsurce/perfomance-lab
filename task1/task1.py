import sys

n = int(sys.argv[1])
m = int(sys.argv[2])


circle_array = list(range(1, n + 1))
path = []
current_index = 0
first = False
while True:
    if current_index == 0 and first:
        break
    first = True
    path.append(circle_array[current_index])
    current_index = (current_index + m - 1) % n
    print(current_index, path)

print(path)
