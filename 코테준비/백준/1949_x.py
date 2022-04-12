import sys

input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split(" ")))
graph = [[] for _ in range(n+1)]
print(people)
for i in range(n - 1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
print(graph)
