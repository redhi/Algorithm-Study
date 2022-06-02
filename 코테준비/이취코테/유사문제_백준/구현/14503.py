# 로봇 청소기
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
dire = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
back = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
ro = {0: 3, 1: 0, 2: 1, 3: 2}
arr = [[] for _ in range(n)]
r, c, d = map(int, input().split())
for i in range(n):
    arr[i].extend(list(map(int, input().split())))
que = deque()
que.append([r, c, d, 0])
arr[r][c] = 2

answer = 1
while que:
    x, y, d, count = que.popleft()
    dd = ro[d]
    d_x, d_y = dire[dd]

    if count == 4:
        b_x, b_y = back[d]
        n_x = x + b_x
        n_y = y + b_y
        if 0 <= n_x < n and 0 <= n_y < m:
            if arr[n_x][n_y] == 1:
                break
            else:
                count = 0
                que.append([n_x, n_y, d, count])
    else:
        n_x = x + d_x
        n_y = y + d_y
        if 0 <= n_x < n and 0 <= n_y < m:
            if arr[n_x][n_y] == 0:
                answer += 1
                arr[n_x][n_y] = 2
                count = 0
                que.append([n_x, n_y, dd, count])
            else:
                count += 1
                que.append([x, y, dd, count])


print(answer)
