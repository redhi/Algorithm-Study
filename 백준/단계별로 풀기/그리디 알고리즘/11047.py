"""
백준 동전 0
"""
import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]

coins.sort(reverse=True)
count = 0

for coin in coins:
    count += K // coin
    K %= coin

print(count)
