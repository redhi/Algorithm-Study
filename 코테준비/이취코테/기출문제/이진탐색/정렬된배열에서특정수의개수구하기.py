import sys

input = sys.stdin.readline
n, x = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

start, end = 0, n - 1
s_idx, e_idx = 0, 0
while start <= end:
    mid = (start + end) // 2
    if n_list[mid] <= x - 1:
        if n_list[mid] == x - 1:
            s_idx = mid
        start = mid + 1
    else:
        end = mid - 1

is_in = False
start, end = 0, n - 1
while start <= end:
    mid = (start + end) // 2
    if n_list[mid] >= x:
        if n_list[mid] == x:
            is_in = True
            break
        end = mid - 1
    else:
        start = mid + 1

start, end = 0, n - 1
while start <= end:
    mid = (start + end) // 2
    if n_list[mid] >= x + 1:
        if n_list[mid] == x + 1:
            e_idx = mid
        end = mid - 1
    else:
        start = mid + 1

if e_idx - s_idx - 1 >= 0:
    print(e_idx - s_idx - 1)
elif is_in:
    print(n - s_idx - 1)
else:
    print(-1)
