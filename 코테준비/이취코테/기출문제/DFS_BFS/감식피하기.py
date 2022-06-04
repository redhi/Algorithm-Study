import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i].extend(list(input().split()))

t_list = []
x_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "T":
            t_list.append([i, j])
        elif arr[i][j] == "X":
            x_list.append((i, j))

candidate = list(map(list, combinations(x_list, 3)))
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
is_ok = False
for c in candidate:
    is_catch = False
    arrr = deepcopy(arr)
    for i in range(3):
        c_x, c_y = c[i]
        arrr[c_x][c_y] = "O"
    que = deque()
    for t in t_list:
        for idx, d in enumerate(dire):
            if is_catch:
                break

            tt = t + [idx]
            que.append(tt)
            while que:
                x, y, dd = que.popleft()

                ddd = dire[dd]
                n_x, n_y = x + ddd[0], y + ddd[1]
                if 0 <= n_x < n and 0 <= n_y < n:
                    if arrr[n_x][n_y] == "X":
                        que.append([n_x, n_y, dd])
                    elif arrr[n_x][n_y] == "S":
                        is_catch = True
                        break

    if not is_catch:
        is_ok = True
        break


if is_ok:
    print("YES")
else:
    print("NO")
