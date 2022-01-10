"""
백준 로프
"""

import sys

input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]


rope.sort(reverse=True)

answer = 0
for i in range(N):
    answer = max(answer, rope[i] * (i + 1))

print(answer)
