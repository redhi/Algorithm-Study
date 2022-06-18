import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

start, end = 0, n_list[-1]
while start <= end:
    mid = (start + end) // 2

    summ = 0
    for nn in n_list:
        if nn > mid:
            summ += nn - mid

    if summ > m:
        start = mid + 1
    else:
        end = mid - 1


print(mid)
