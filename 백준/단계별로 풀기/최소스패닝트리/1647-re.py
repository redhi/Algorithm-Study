"""
도시분할계획
"""


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = [i for i in range(N + 1)]


def find(node):
    if parent[node] == node:
        return parent[node]
    else:
        return find(parent[node])


result = 0
max_arr = []


def union(graph):
    global result
    c, a, b = graph
    p_a = find(a)
    p_b = find(b)

    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b


for i in range(len(graph)):
    if find(a) != find(b):
        union(graph[i])
        c = graph[i][0]
        result += c
        max_arr.append(c)

result -= max_arr.pop()
print(result)
