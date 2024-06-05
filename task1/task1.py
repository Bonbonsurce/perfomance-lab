import numpy as np

n, m = map(int, input().split())

circle_array = np.arange(1, n+1)
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