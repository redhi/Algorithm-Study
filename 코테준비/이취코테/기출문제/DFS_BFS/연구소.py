import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
que = deque()

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, input().split())))

zero_list = []
two_list = []
one = 0
two = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero_list.append((i, j))
        elif arr[i][j] == 1:
            one += 1
        else:
            two_list.append((i, j))
            two += 1
one += 3
candidate = list(map(list, combinations(zero_list, 3)))
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 0
for c in candidate:
    arrr = deepcopy(arr)
    for z in c:
        z_x, z_y = z
        arrr[z_x][z_y] = 1
    count = 0
    for twoo in two_list:
        que.append([twoo[0], twoo[1]])
        while que:
            x, y = que.popleft()
            for d in dire:
                n_x, n_y = x + d[0], y + d[1]
                if 0 <= n_x < n and 0 <= n_y < m:
                    if arrr[n_x][n_y] == 0:
                        arrr[n_x][n_y] = 2
                        count += 1
                        que.append([n_x, n_y])
    total = m * n - (one + two + count)

    answer = max(answer, total)

print(answer)
