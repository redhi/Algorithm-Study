import sys
import heapq

N = int(input())
myheap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(myheap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(myheap))
        except:
            print(0)
