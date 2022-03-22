import sys

input = sys.stdin.readline

V, E = map(int, input().split())

graph = []
for i in range(E):
    A, B, C = map(int, input().split())
    graph.append([C, A, B])
graph.sort()

parent = [i for i in range(V + 1)]

merge = 0


def union_find(node):
    global merge
    A = node[1]
    B = node[2]
    C = node[0]
    p_A = find(A)
    p_B = find(B)
    if p_A != p_B:
        parent[p_B] = p_A
        merge += C


def find(node):
    if parent[node] == node:
        return parent[node]
    else:
        return find(parent[node])


for i in range(len(graph)):
    union_find(graph[i])


print(merge)
