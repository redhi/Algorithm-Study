"""
백준 그룹 단어 체커
구현, 문자열
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

count = 0
for _ in range(N):
    visited = []
    word = deque(input().rstrip())
    w = word.popleft()
    group = True

    visited.append(w)
    while word:
        w = word.popleft()
        if w not in visited or visited[-1] == w:
            visited.append(w)
        else:
            group = False
            break
    if group:
        count += 1

print(count)
