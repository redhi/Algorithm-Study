import sys
from collections import deque

input = sys.stdin.readline

s = list(map(int, list(input().rstrip())))

que = deque(s)
while que:
    if len(que) == 1:
        print(que.popleft())
        break
    a = que.popleft()
    b = que.popleft()
    if a == 0 or b == 0:
        que.appendleft(a + b)
    else:
        que.appendleft(a * b)
