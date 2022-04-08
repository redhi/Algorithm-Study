import copy
import sys
from collections import deque


def check(now_arr, virus):
    que1 = deque()
    for v in virus:
        v_x, v_y = v
        que1.append([v_x, v_y, now_arr])
    total = 0
    while que1:
        x, y, arr1 = que1.popleft()
        for d in direction:
            now_x = x + d[0]
            now_y = y + d[1]
            if 0 <= now_x < n and 0 <= now_y < m:
                if arr1[now_x][now_y] == 0:
                    arr1[now_x][now_y] = 2
                    que1.append([now_x, now_y, arr1])
                    total += 1
    return total


def dfs(count):
    global max_safe, default_num, n
    if count == 3:
        arr_nw = copy.deepcopy(arr)
        check(arr_nw, virus)
        safe_num = 0
        for i in range(n):
            safe_num += arr_nw[i].count(0)
        if max_safe < safe_num:
            max_safe = safe_num
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(count + 1)
                arr[i][j] = 0


virus = []
max_safe = 0
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n)]

for i in range(n):
    column = list(map(int, input().split()))
    for j in range(m):
        if column[j] == 2:
            virus.append([i, j])
    arr[i].extend(column)

dfs(0)
print(max_safe)
