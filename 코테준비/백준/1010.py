# 다리 놓기
import sys
from math import comb

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(comb(b, a))
