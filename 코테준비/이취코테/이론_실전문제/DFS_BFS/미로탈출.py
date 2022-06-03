import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, list(input().rstrip()))))
print(arr)
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
que = deque()
que.append([0, 0, 1])
while que:
    x, y, count = que.popleft()
    if x == n - 1 and y == m - 1:
        print(count)
        break
    for d in dire:
        n_x = x + d[0]
        n_y = y + d[1]
        if 0 <= n_x < n and 0 <= n_y < m:
            if arr[n_x][n_y] == 1:
                arr[n_x][n_y] = 2
                que.append([n_x, n_y, count + 1])
