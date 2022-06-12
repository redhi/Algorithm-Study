"""
백준 N-Queen
"""

import sys

input = sys.stdin.readline
N = int(input())

visit = [0] * N
result = 0


def find(count):
    for j in range(count):
        if visit[count] == visit[j] or abs(visit[count] - visit[j]) == abs(count - j):
            return False
    return True


def dfs(count):
    global result
    if count == N:
        result += 1
        return
    else:
        for i in range(N):
            visit[count] = i
            if find(count):
                dfs(count + 1)
                visit[count] = 0


dfs(0)
print(result)
