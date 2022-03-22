"""
백준 파티
"""

import heapq
import sys

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

heap = []


def di(start):
    d = [1000000001] * (N + 1)
    d[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        value, node = heapq.heappop(heap)
        if d[node] < value:
            continue
        for next_v, next in graph[node]:
            next_w = value + next_v
            if next_w < d[next]:
                d[next] = next_w
                heapq.heappush(heap, [next_w, next])
    print(d)
    # for i in range(len(graph[node])):
    #     heapq.heappush(heap, [graph[node][0], graph[node][1]])
    #     d[graph[node][1]] = graph[node][0]


for i in range(1, N + 1):
    di(i)
di(1)
