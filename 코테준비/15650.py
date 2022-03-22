"""
백준 N과 M(2)
"""
import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().split())

num = [i for i in range(1, N + 1)]
num_list = list(permutations(num, M))
for i in range(len(num_list)):
    is_high = num_list[i][0]
    count = 0
    for j in range(len(num_list[i])):
        if is_high < num_list[i][j]:
            is_high = num_list[i][j]
            count += 1
    if count == len(num_list[i]) - 1:
        print(" ".join(map(str, num_list[i])))

        # print(num_list[i][j])

# while len(stack) != N:
#     visited = [0 for i in range(N+1)]
#     for i in range(1, N+1):
#         stack.append(i)

# import sys
# read = sys.stdin.readline

# n, m = map(int, read().split())

# a = []

# def dfs(start) :
#     if (len(a) == m) :
#         print(' '.join(map(str, a)))
#         return
#     for i in range(start, n+1) :
#         a.append(i)
#         dfs(i+1)
#         a.pop()
# dfs(1)

# def dfs(start):
#     if len(a) == m:
#         print(" ".join(map(str, a)))
#         return
#     for i in range(start, n+1):
#         a.append(i)
#         dfs(i+1)
#         a.pop()
# a = []
# def dfs(count):

#     visit = [0 for _ in range(N+1)]
#     if count == m:
#         print(" ".join(map(str, a)))
#         return
#     for i in range(1, N+1):
#         if visit[i] == 0 and (a[-1] < i or len(a)== 0):
#             visit[i] = 1
#             a.append(i)
#             dfs(count+1)
#             visit[i] = 0
#             a.pop()
