"""
백준 도시 분할 계획
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()
result = 0

parent = [i for i in range(N + 1)]


def union(a, b):
    global result
    # value, a, b = graph[i]
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        parent[p_b] == p_a


def find(node):
    if parent[node] == node:
        return parent[node]
    else:
        return find(parent[node])


selected = []
for value, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += value
        selected.append(value)
result -= selected.pop()
print(result)
