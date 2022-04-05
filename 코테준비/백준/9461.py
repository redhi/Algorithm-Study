import sys

input = sys.stdin.readline

n = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
dp2 = [0] * 100
dp.extend(dp2)
answer = []
for i in range(n):
    num = int(input())
    if num > 10:
        for i in range(10, num + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
    answer.append(dp[num - 1])
    
for i in range(len(answer)):
    print(answer[i])
