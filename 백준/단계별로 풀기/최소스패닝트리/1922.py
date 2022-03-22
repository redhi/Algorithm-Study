"""
백준 네트워크 연결
"""

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()
parent = [i for i in range(N + 1)]


def find(node):
    if parent[node] == node:
        return node
    else:
        return find(parent[node])


result = 0

for i in range(len(graph)):
    a = graph[i][1]
    b = graph[i][2]
    c = graph[i][0]
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        result += c
        parent[p_b] = p_a


print(result)
