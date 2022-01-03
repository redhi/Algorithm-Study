"""
백준 연속합
앞전의 합 + 이번 수, 이번 수 중 큰 값을 구함
-> 연속된 합을 구할 수 있음
"""

import sys

input = sys.stdin.readline

N = int(input())
my_list = list(map(int, input().split()))


d = []
d.append(my_list[0])
for i in range(len(my_list) - 1):
    d.append(max(d[i] + my_list[i + 1], my_list[i + 1]))

print(max(d))
