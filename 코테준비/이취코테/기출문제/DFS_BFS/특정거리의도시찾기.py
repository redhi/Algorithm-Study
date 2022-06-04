import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

que = deque()
visit[x] = 1
que.append([x, 0])
answer = []
while que:
    start, count = que.popleft()
    if count == k:
        answer.append(start)
    for i in range(len(graph[start])):
        if visit[graph[start][i]] == 0:
            visit[graph[start][i]] = 1
            que.append([graph[start][i], count + 1])

answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)
