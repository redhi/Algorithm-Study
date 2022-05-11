# A와 B
import sys
from collections import deque

input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()

t = T
que = deque()
que.append(T)

result = 0
while que:
    tt = que.popleft()

    if tt == S:
        result = 1
        break
    if tt[-1] == "B":
        ttt = tt[:-1]
        ttt = ttt[::-1]
        if ttt:
            que.append(ttt)
    if tt[-1] == "A":
        ttt = tt[:-1]
        if ttt:
            que.append(ttt)

print(result)
