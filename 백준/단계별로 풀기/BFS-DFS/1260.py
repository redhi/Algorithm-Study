"""
백준 DFS와 BFS
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# graph = deque()

visited_bfs = []
visited_bfs.append(V)
visited_dfs = []
visited_dfs.append(V)


def dfs():
    graph[V].sort(reverse=True)
    need = deque(graph[V])
    while need:
        node = need.pop()
        if node in visited_dfs:
            continue
        visited_dfs.append(node)
        graph[node].sort(reverse=True)
        need = need + deque(graph[node])
    print(" ".join(map(str, visited_dfs)))


def bfs():
    graph[V].sort()
    need = deque(graph[V])
    while need:
        node = need.popleft()
        if node in visited_bfs:
            continue
        visited_bfs.append(node)
        graph[node].sort()
        need = need + deque(graph[node])
    print(" ".join(map(str, visited_bfs)))


dfs()
bfs()
