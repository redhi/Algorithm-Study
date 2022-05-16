# 집합
import sys

input = sys.stdin.readline
M = int(input())

s = []
for i in range(M):
    l = list(input().split())
    if len(l) == 2:
        type, num = l
        num = int(num)
    else:
        type = l[0]

    if type == "add":
        s.append(num)
        s = set(s)
        s = list(s)
    if type == "remove":
        if num in s:
            s.remove(num)
    if type == "check":
        if num in s:
            print(1)
        else:
            print(0)
    if type == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.append(num)
    if type == "all":
        s = [i + 1 for i in range(20)]
    if type == "empty":
        s = []
