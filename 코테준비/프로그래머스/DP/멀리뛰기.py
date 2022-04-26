a = []
count = 0


def solution(n):
    dp = [0 for _ in range(2001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
   
    return dp[n]


# a = []
# count = 0


# def dfs(n):
#     global count
#     if sum(a) >= n:
#         if sum(a) == n:
#             count += 1
#             count %= 1234567
#             print(a)
#         return
#     for i in range(1, 3):
#         a.append(i)
#         dfs(n)
#         a.pop()


# def solution(n):
#     global count
#     dfs(n)
#     return count


# 1 2 3 5 8 13
# 1 1 1 1
# 1 2 1
# 1 1 2
n = 1
print(solution(n))
