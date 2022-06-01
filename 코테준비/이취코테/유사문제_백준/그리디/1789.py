# 수들의 합
import sys

input = sys.stdin.readline

s = int(input())
num = 1
while True:
    summ = (num * (num + 1)) // 2
    if summ > s:
        break
    num += 1

print(num - 1)
