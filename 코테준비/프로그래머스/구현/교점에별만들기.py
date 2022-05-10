def intersect(line1, line2):
    a, b, c = line1
    d, e, f = line2
    if a * e - b * d == 0:
        return None
    x = (b * f - e * c) / (a * e - b * d)
    y = (c * d - f * a) / (a * e - b * d)
    if x.is_integer() and y.is_integer():
        return (int(x), int(y))


def solution(line):
    points = set()
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            point = intersect(line[i], line[j])
            if point:
                points.add(point)

    xp = [p[0] for p in points]
    x_min, x_max = min(xp), max(xp)
    yp = [p[1] for p in points]
    y_min, y_max = min(yp), max(yp)
    arr = [["." for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    for p in points:
        x, y = p
        arr[y_max - y][x - x_min] = "*"
    arr = ["".join(p) for p in arr]
    return arr


# 4x=0

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))
