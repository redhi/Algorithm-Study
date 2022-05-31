import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
que = deque(arr)
count = 0
while que:
    num = que.popleft()
    if len(que) < (num - 1):
        break
    for i in range(num - 1):
        que.popleft()
    count += 1

print(count)
