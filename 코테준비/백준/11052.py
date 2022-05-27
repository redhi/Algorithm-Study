# 카드 구매하기
import sys

input = sys.stdin.readline

N = int(input())

pay_list = [0] + list(map(int, input().split()))
dp = [0 for i in range(len(pay_list))]
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], pay_list[j] + dp[i - j])

print(dp[N])
