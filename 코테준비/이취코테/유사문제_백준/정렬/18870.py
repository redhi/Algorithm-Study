# 좌표 압축
import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, [arr[i], i])
pre = heapq.heappop(heap)

answer = [0 for _ in range(n)]
count = 0

while heap:
    a = heapq.heappop(heap)
    if pre[0] != a[0]:
        count += 1
        answer[a[1]] = count
        pre = a
    else:
        answer[a[1]] = count
print(*answer)
