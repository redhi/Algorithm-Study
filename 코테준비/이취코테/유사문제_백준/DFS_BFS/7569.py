# 토마토
import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

ripe_list = []
total = m * n * h
count = 0
for i in range(h - 1, -1, -1):
    for j in range(n):
        temp = list(map(int, input().split()))
        for k in range(m):
            if temp[k] == 1:
                count += 1
                ripe_list.append([i, j, k, 0])
            if temp[k] == -1:
                total -= 1
            box[i][j][k] = temp[k]

que = deque()
dire = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1],
]
if total - count == 0:
    print(0)
else:
    for ripe in ripe_list:
        que.append(ripe)
    is_in = False
    while que:
        z, x, y, day = que.popleft()
        if is_in:
            break

        for d in dire:
            n_z, n_x, n_y = z + d[0], x + d[1], y + d[2]
            if 0 <= n_z < h and 0 <= n_x < n and 0 <= n_y < m:
                if box[n_z][n_x][n_y] == 0:
                    box[n_z][n_x][n_y] = 1
                    que.append([n_z, n_x, n_y, day + 1])
                    count += 1
                    if total - count == 0:
                        print(day + 1)
                        is_in = True
                        break
    if not is_in:
        print(-1)
