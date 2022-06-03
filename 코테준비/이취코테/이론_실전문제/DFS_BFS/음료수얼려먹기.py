import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, list(input().rstrip()))))
que = deque()


dire = [[0, -1], [0, 1], [1, 0], [-1, 0]]
count = 0
for i in range(n):
    for j in range(m):
        que.append([i, j])
        is_in = False
        while que:
            x, y = que.popleft()
            for d in dire:
                n_x = x + d[0]
                n_y = y + d[1]
                if 0 <= n_x < n and 0 <= n_y < m:
                    if arr[n_x][n_y] == 0:
                        is_in = True
                        arr[n_x][n_y] = 1
                        que.append([n_x, n_y])

        if is_in:
            count += 1
print(count)
