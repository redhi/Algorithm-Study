# 다리 놓기
import sys
from math import factorial

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(a) * factorial(b - a)))
