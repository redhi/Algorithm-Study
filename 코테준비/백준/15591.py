import sys
from collections import deque

input = sys.stdin.readline
n, q = map(int, input().split())

video_arr = [[] for _ in range(n + 1)]
for i in range(n - 1):
    p, q_i, r = map(int, input().split())
    video_arr[p].append([r, q_i])
    video_arr[q_i].append([r, p])

for i in range(n + 1):
    video_arr[i].sort(reverse=True)

que = deque()
for _ in range(q):
    k, v = map(int, input().split())
    count = 0
    visit = [0] * (n + 1)
    que.append(v)
    visit[v] = 1
    while que:
        node = que.popleft()
        for j in range(len(video_arr[node])):
            if visit[video_arr[node][j][1]] == 0:
                if video_arr[node][j][0] >= k:
                    count += 1
                    que.append(video_arr[node][j][1])
                    visit[video_arr[node][j][1]] = 1
                else:
                    break
    print(count)
