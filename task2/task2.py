from math import sqrt


def distance(x_, y_):
    return sqrt(pow((x - x_), 2) + pow((y - y_), 2))


# circle_params_path = 'circle_rad_cen.txt'
# dots_params_path = 'dots.txt'

circle_params_path = input()
dots_params_path = input()

with open(circle_params_path, 'r') as file:
    x, y = map(float, file.readline().strip().split())
    r = float(file.readline().strip())

with open(dots_params_path, 'r') as file:
    for line in file:
        px, py = map(float, line.strip().split())
        if distance(px, py) > r:
            print(2)
        elif distance(px, py) == r:
            print(0)
        else:
            print(1)
