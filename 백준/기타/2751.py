"""
백준 수 정렬하기 2
"""

import sys

input = sys.stdin.readline

N = int(input())
my_list = [int(input()) for _ in range(N)]
my_list.sort()
for i in my_list:
    sys.stdout.write(i)
