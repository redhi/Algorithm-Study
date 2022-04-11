import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
que = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(i):
    visit = [0] * (n + 1)
    que.append(i)
    visit[i] = 1
    count = 1
    while que:
        node = que.popleft()

        for j in graph[node]:
            if visit[j] == 0:
                visit[j] = 1
                que.append(j)
                count += 1

    return count


answer = []
for i in range(n):
    answer.append(bfs(i + 1))
max_num = max(answer)
for i in range(len(answer)):
    if max_num == answer[i]:
        print(i + 1, end=" ")
