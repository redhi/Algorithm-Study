# 가스관
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
arr = [[] for _ in range(R)]
M_idx = Z_idx = [0, 0]
for i in range(R):
    s = input().rstrip()
    if s.find("M") != -1:
        M_idx = [i, s.find("M")]
    if s.find("Z") != -1:
        Z_idx = [i, s.find("Z")]

    arr[i].extend(list(s))

print(arr, M_idx, Z_idx)
visit = [[0 for _ in range(C)] for _ in range(R)]


def dfs(y, x, visit):
    dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if y == Z_idx[0] and x == Z_idx[1]:
        return
    for d in dire:
        now_y = d[0] + y
        now_x = d[1] + x
        if 0 <= now_y < R and 0 <= now_x < C:
            if arr[now_y][now_x] != "." and visit[now_y][now_x] == 0:
                if arr[now_y][now_x] == "-":
                    if d == [0, -1] or d == [0, 1]:
                        visit[now_y][now_x] = 1
                        return dfs(now_y, now_x, visit)
                if arr[now_y][now_x] == "|":
                    if d == [-1, 0] or d == [1, 0]:
                        visit[now_y][now_x] = 1
                        return dfs(now_y, now_x, visit)
                if arr[now_y][now_x] == "1":
                    if d == [-1, 0] or d == [1, 0]:
                        visit[now_y][now_x] = 1
                        return dfs(now_y, now_x, visit)


visit[M_idx[0]][M_idx[1]] = 1
dfs(M_idx[0], M_idx[1], visit)
