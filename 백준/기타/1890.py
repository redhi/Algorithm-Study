"""
백준 점프
DP
"""

import sys

input = sys.stdin.readline

N = int(input())
game_list = [list(map(int, input().split(" "))) for _ in range(N)]

# 아래로 [i][j] -> [i+n][j]
# 오른쪽으로 [i][j] -> [j][j+n]
d = [[0] * N for _ in range(N)]
d[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(d[i][j])
            break

        # 아래
        if game_list[i][j] + i < N:
            d[i + game_list[i][j]][j] += d[i][j]
        # 오른쪽
        if game_list[i][j] + j < N:
            d[i][j + game_list[i][j]] += d[i][j]
