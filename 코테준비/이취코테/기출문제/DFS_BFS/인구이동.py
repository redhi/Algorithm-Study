import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i].extend(list(map(int, input().split())))
que = deque()
que.append([0, 0])
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]

answer = 0
while True:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    total = []
    for i in range(n):
        for j in range(n):
            que.append([i, j])
            visit[i][j] = 1
            summ_list = [[i, j]]
            summ = arr[i][j]
            while que:
                x, y = que.popleft()
                for d in dire:
                    n_x, n_y = x + d[0], y + d[1]
                    if 0 <= n_x < n and 0 <= n_y < n:
                        if visit[n_x][n_y] == 0:
                            minus_between = abs(arr[x][y] - arr[n_x][n_y])
                            if l <= minus_between and minus_between <= r:
                                visit[n_x][n_y] = 1
                                que.append([n_x, n_y])
                                summ_list.append([n_x, n_y])
                                summ += arr[n_x][n_y]
            if len(summ_list) != 1:
                total.append([summ_list, summ])

    if not total:
        break

    for t in total:
        summ_list, summ = t[0], t[1]
        num = summ // len(summ_list)
        for ss in summ_list:
            arr[ss[0]][ss[1]] = num

    answer += 1

print(answer)
