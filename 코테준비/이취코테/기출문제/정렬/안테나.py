import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if len(arr) % 2 == 0:
    idx = len(arr) // 2 - 1
else:
    idx = len(arr) // 2

print(arr[idx])


# 1 3 9 12
