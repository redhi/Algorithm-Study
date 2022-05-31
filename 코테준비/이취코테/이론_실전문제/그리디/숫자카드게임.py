import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    a_min = min(a)
    arr.append(a_min)

print(max(arr))
