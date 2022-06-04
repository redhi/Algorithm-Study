import sys

input = sys.stdin.readline
n, k = map(int, input().split())
num_list = [[] for _ in range(k + 1)]

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, input().split())))
s, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            num_list[arr[i][j]].append((i, j))

dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(s):
    for j in range(1, k + 1):
        new = []
        for z in range(len(num_list[j])):
            xx, yy = num_list[j][z]
            for d in dire:
                n_x, n_y = xx + d[0], yy + d[1]
                if 0 <= n_x < n and 0 <= n_y < n:
                    if arr[n_x][n_y] == 0:
                        new.append((n_x, n_y))
                        arr[n_x][n_y] = j

        num_list[j] = new

print(arr[x - 1][y - 1])
