# 테트로미트
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n)]


for i in range(n):
    arr[i].extend(list(map(int, input().split())))

pol = [
    [[0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [1, 0], [1, 1]],
    [[1, 0], [2, 0], [2, 1]],
    [[1, 0], [2, 0], [2, -1]],
    [[0, 1], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [1, -2]],
    [[0, 1], [0, 2], [1, 0]],
    [[1, 0], [1, 1], [2, 1]],
    [[0, 1], [-1, 1], [-1, 2]],
    [[1, 0], [1, -1], [2, -1]],
    [[0, 1], [1, 1], [1, 2]],
    [[0, 1], [0, 2], [1, 1]],
    [[-1, 1], [0, 1], [2, 1]],
    [[1, 0], [1, 1], [2, 0]],
    [[1, -1], [1, 0], [1, 1]],
]
answer = 0
for i in range(n):
    for j in range(m):
        for p in pol:
            a, b, c = p
            a_x, a_y = a
            b_x, b_y = b
            c_x, c_y = c
            aa_x, aa_y = i + a_x, j + a_y
            bb_x, bb_y = i + b_x, j + b_y
            cc_x, cc_y = i + c_x, j + c_y
            summ = 0
            if (
                0 <= aa_x < n
                and 0 <= aa_y < m
                and 0 <= bb_x < n
                and 0 <= bb_y < m
                and 0 <= cc_x < n
                and 0 <= cc_y < m
            ):
                summ = arr[i][j] + arr[aa_x][aa_y] + arr[bb_x][bb_y] + arr[cc_x][cc_y]
                answer = max(answer, summ)
print(answer)
