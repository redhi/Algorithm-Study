import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x: x[1])
for s, n in arr:
    print(s, end=" ")
