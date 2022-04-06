import sys

input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(n)]

for i in range(n):
    col = list(input().rstrip())
    arr[i].extend(col)


def col_check(arr, x, y):
    max_num = 0
    new_arr = list(map(list, zip(*arr)))

    max1, max2, max3 = 1, 1, 1
    max_list = [[] for _ in range(3)]
    for i in range(len(new_arr) - 1):
        if new_arr[x][i] == new_arr[x][i + 1]:
            max1 += 1
        else:
            max_list[0].append(max1)
            max1 = 1
        if new_arr[x + 1][i] == new_arr[x + 1][i + 1]:
            max2 += 1
        else:
            max_list[1].append(max2)
            max2 = 1
        if arr[y][i] == arr[y][i + 1]:
            max3 += 1
        else:
            max_list[2].append(max3)
            max3 = 1
    max_list[0].append(max1)
    max_list[1].append(max2)
    max_list[2].append(max3)

    max1 = max(max_list[0])
    max2 = max(max_list[1])
    max3 = max(max_list[2])

    max_num = max(max1, max2, max3)
    return max_num


def row_check(arr, x, y):
    max_num = 0
    new_arr = list(map(list, zip(*arr)))

    max1, max2, max3 = 1, 1, 1
    max_list = [[] for _ in range(3)]
    for i in range(len(new_arr) - 1):
        if arr[y][i] == arr[y][i + 1]:
            max1 += 1
        else:
            max_list[0].append(max1)
            max1 = 1
        if arr[y + 1][i] == arr[y + 1][i + 1]:
            max2 += 1
        else:
            max_list[1].append(max2)
            max2 = 1
        if new_arr[x][i] == new_arr[x][i + 1]:
            max3 += 1
        else:
            max_list[2].append(max3)
            max3 = 1

    max_list[0].append(max1)
    max_list[1].append(max2)
    max_list[2].append(max3)

    max1 = max(max_list[0])
    max2 = max(max_list[1])
    max3 = max(max_list[2])
    max_num = max(max1, max2, max3)
    return max_num


maxx = 0
for y in range(n):
    for x in range(n - 1):
        arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x]
        max_num = col_check(arr, x, y)
        maxx = max(max_num, maxx)
        arr[y][x + 1], arr[y][x] = arr[y][x], arr[y][x + 1]

for x in range(n):
    for y in range(n - 1):
        arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x]
        max_num = row_check(arr, x, y)
        maxx = max(max_num, maxx)
        arr[y + 1][x], arr[y][x] = arr[y][x], arr[y + 1][x]

print(maxx)
