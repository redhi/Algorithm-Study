import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
answer = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    summ = a + b
    answer += summ
    heapq.heappush(heap, summ)

print(answer)
