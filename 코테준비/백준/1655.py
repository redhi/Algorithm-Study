import heapq
import sys

input = sys.stdin.readline
n = int(input())

leftheap = []
rightheap = []
for i in range(n):
    num = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)

    if rightheap and rightheap[0] < -leftheap[0]:
        l = heapq.heappop(leftheap)
        r = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -r)
        heapq.heappush(rightheap, -l)
    print(-leftheap[0])
