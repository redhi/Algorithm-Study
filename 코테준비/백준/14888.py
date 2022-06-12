"""
백준 연산자 끼워넣기
"""

import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper2 = []

result = []
count = 0
r_max = -10000000000
r_min = 10000000000


def dfs(count):
    global r_max
    global r_min
    if count == (N - 1):
        real = num[0]

        for i in range(1, len(num)):
            if result[i - 1] == 0:
                real += num[i]
            if result[i - 1] == 1:
                real -= num[i]
            if result[i - 1] == 2:
                real *= num[i]
            if result[i - 1] == 3:
                if real < 0:
                    real = -(abs(real) // num[i])
                else:
                    real //= num[i]
        r_min = min(r_min, real)
        r_max = max(r_max, real)

        return
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            result.append(i)
            dfs(count + 1)
            oper[i] += 1
            result.pop()


dfs(0)

print(r_max)
print(r_min)
