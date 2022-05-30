# 촌수계산
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
m = int(input())
family = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

que = deque()
visit = [0 for _ in range(n + 1)]
visit[target[0]] = 1
que.append([target[0], target[1], visit, 0])
answer = -1
while que:
    start, end, visit, count = que.popleft()
    if start == end:
        answer = count
        break

    for j in range(len(family[start])):
        if visit[family[start][j]] == 0:
            visit[family[start][j]] = 1
            que.append([family[start][j], end, visit, count + 1])

print(answer)
