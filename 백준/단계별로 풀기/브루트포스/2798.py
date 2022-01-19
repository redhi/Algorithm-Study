"""
백준 블랙잭
"""

import itertools
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
nCr = list(itertools.combinations(cards, 3))

max_num = 0
for i in nCr:
    if sum(i) <= M:
        max_num = max(max_num, sum(i))
print(max_num)
