import heapq
import sys

N = int(input())
myheap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if not myheap:
            print(0)
        else:
            print(heapq.heappop(myheap))
    else:
        heapq.heappush(myheap, num)
