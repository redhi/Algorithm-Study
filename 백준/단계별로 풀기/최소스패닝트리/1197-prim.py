"""
Prim을 이용해 풀이
"""
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

heap = []
result = 0

visited = [0] * (V + 1)
# print(visited)
# print(graph)


def prim(a):
    global result
    # visited[a] = 1
    heapq.heappush(heap, (0, 1))

    while heap:
        wei, node = heapq.heappop(heap)

        if visited[node] == 0:
            visited[node] = 1

            result += wei
            for i in range(len(graph[node])):
                heapq.heappush(heap, (graph[node][i][0], graph[node][i][1]))


prim(1)
print(result)
