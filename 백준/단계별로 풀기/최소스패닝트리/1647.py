"""
백준 도시 분할 계획
"""

import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visit = [0] * (M + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


heap = []
result = 0
selected = []


def prim(start):
    global result

    heapq.heappush(heap, [0, start])

    while len(heap) != 0:
        value, node = heapq.heappop(heap)

        if visit[node] == 0:
            visit[node] = 1
            result += value
            selected.append(value)

            for i in range(len(graph[node])):
                heapq.heappush(heap, [graph[node][i][0], graph[node][i][1]])

    result -= selected.pop()


prim(1)
print(result)
