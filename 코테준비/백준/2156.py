import sys

input = sys.stdin.readline

n = int(input())
answer = 0
wine_list = [0]

for i in range(n):
    wine = int(input())
    wine_list.append(wine)

dp = [0] * (n + 1)
if n <= 2:
    answer = sum(wine_list)
else:
    dp[1] = wine_list[1]
    dp[2] = wine_list[1] + wine_list[2]

    for i in range(3, len(wine_list)):
        dp[i] = max(
            wine_list[i - 1] + wine_list[i] + dp[i - 3],
            dp[i - 2] + wine_list[i],
            dp[i - 1],
        )

    answer = dp[n]
print(answer)
