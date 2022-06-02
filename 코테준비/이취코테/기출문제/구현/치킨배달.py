import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
house = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = temp[j]
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))
candidate = list(map(list, combinations(chicken, m)))

r_len = int(1e9)
for can in candidate:
    s_len = 0
    for h in house:
        h_x, h_y = h
        c_len = int(1e9)
        for c in can:
            c_x, c_y = c
            t = abs(h_x - c_x) + abs(h_y - c_y)
            c_len = min(c_len, t)
        s_len += c_len
    r_len = min(r_len, s_len)
print(r_len)
