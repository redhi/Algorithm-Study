"""
다시 풀기
"""
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
print(graph)
d = [100000001] * (V + 1)
start = graph[K].sort()
wei, s_node = start[0]
d[K] = 0
heap = []
heapq.heappush(heap, (0, K))
while heap:
    wei, node = heapq.heappop(heap)
    if d[node] < wei:
        continue
    for i in range(len(graph[node])):
        wei, node = graph[node][i]
