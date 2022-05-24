# A -> B
import sys
from collections import deque

input = sys.stdin.readline
A, B = map(int, input().split())

que = deque()
que.append([A, 1])
answer = int(1e9)

while que:
    now, count = que.popleft()
    if now == B:
        answer = min(answer, count)
    now1 = now * 2
    now2 = int(str(now) + "1")
    if now1 <= B:
        que.append([now1, count + 1])
    if now2 <= B:
        que.append([now2, count + 1])

if answer == int(1e9):
    answer = -1

print(answer)
