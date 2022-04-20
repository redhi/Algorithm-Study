import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
max_str = ""
min_str = ""
if len(a) > len(b):
    max_str = a
    min_str = b
else:
    max_str = b
    min_str = a
answer = 0
dp = [[0 for _ in range(len(min_str) + 1)] for _ in range(len(max_str) + 1)]
for i in range(1, len(max_str) + 1):
    for j in range(1, len(min_str) + 1):
        if max_str[i - 1] == min_str[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(dp[i][j], answer)
print(answer)
# min_list = list(min_str)
# for i in range(len(min_list)):
#     if max_str.find(min_list[i]) > -1:
#         dp[0].append([i, i])

# answer = 0
# for i in range(len(dp)):
#     if len(dp[i]) == 0:
#         answer = i
#         break
#     for j in range(len(dp[i])):
#         s, e = dp[i][j]
#         if e + 1 != len(min_str):
#             e += 1
#             if max_str.find(min_str[s : e + 1]) > -1:
#                 dp[i + 1].append([s, e])
# print(dp)

print(answer)
