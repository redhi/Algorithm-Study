import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, input().split())))
arr[x][y] = 1
que = deque()
que.append([x, y, d])

count = 1
dic = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}
dd = {0: [0, 3, 2, 1], 1: [1, 0, 3, 2], 2: [2, 1, 0, 3], 3: [3, 2, 1, 0]}
back = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}

while que:
    n_x, n_y, dire = que.popleft()

    dir = dd[dire]
    is_in = False
    for d in dir:
        xx, yy = dic[d]
        new_x = n_x + xx
        new_y = n_y + yy

        if 0 <= new_x < m and 0 <= new_y < n:
            if arr[new_x][new_y] == 0:
                is_in = True
                arr[new_x][new_y] = 2
                count += 1
                que.append([new_x, new_y, d])
                break
    if not is_in:
        b_x, b_y = back[d]
        nn_x = n_x + b_x
        nn_y = n_y + b_y
        if 0 <= nn_x < m and 0 <= nn_y < n:
            if arr[nn_x][nn_y] != 1:
                que.append([nn_x, nn_y, d])


print(count)
# 1 : 바다, 0 : 육지
# 서 - 동
# 왼
