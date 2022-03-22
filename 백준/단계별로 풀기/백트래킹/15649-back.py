"""
백준 N과 M(1)
백트래킹
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]
num = 1
for i in range(M):
    num = num * (N - i)
print(num)
stack = deque()
result = []
visit = [0] * (N + 1)
print(len(result))
print(arr)
while len(result) != num:
    print("잉??????")
    if len(stack) == M:
        if list(stack) in result:
            pass
        else:
            result.append(list(stack))
            node = stack.pop()
            visit[node] = 0
            if node != N:
                stack.append(node + 1)
                visit[node] = 1
            else:
                node = stack.pop()

    if len(stack) != M:
        print("아하ㅏ!")
        for i in range(1, N + 1):
            if visit[i] == 0:
                visit[i] = 1
                stack.append(i)
                break

    print(visit)
    print(stack)
    print(result)
