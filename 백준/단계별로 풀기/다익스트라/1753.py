import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

heapq.heappush(heap, (0, K))
route = [300000] * (V + 1)
route[K] = 0
while heap:
    w, node = heapq.heappop(heap)
    if route[node] < w:
        continue

    for wei, next in graph[node]:
        next_w = w + wei

        if next_w < route[next]:
            route[next] = next_w
            heapq.heappush(heap, (next_w, next))


for i in range(1, len(route)):
    if route[i] == 300000:
        print("INF")
    else:
        print(route[i])
