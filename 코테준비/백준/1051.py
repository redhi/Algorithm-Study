import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip())))
max_len = min(n, m)
is_max = False
answer = 0
for ma in range(max_len, 0, -1):
    if is_max:
        break
    for i in range(n):
        if is_max:
            break
        for j in range(m):
            if is_max:
                break
            if 0 <= i + ma - 1 < n and 0 <= j + ma - 1 < m:
                num = arr[i][j]
                now_i = i + ma - 1
                now_j = j + ma - 1
                if (
                    num == arr[now_i][j]
                    and num == arr[i][now_j]
                    and num == arr[now_i][now_j]
                ):
                    answer = ma * ma
                    is_max = True
                    break

print(answer)
