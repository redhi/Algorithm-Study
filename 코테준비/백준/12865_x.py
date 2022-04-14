import sys
from collections import deque

# from turtle import back

input = sys.stdin.readline

n, k = map(int, input().split())
backpack = []
dic = dict()
dp = [0] * (k + 1)
print(dp)
for i in range(n):
    w, v = map(int, input().split())
    backpack.append([w, v / w])
    dic[w] = v
    dp[w] = max(dp[w], v)
backpack.sort(key=lambda x: (x[0], -x[1]))
print(backpack)

a = [0]
print(dp)
visit = [0] * (n)
# for i in range(1,k+1):
#     for j in range(1,i):
#         dp[i] =

max_num = 0


def dfs():
    global max_num
    if sum(a) >= k:
        summ = 0
        if sum(a) > k:
            num = a.pop()
            for i in range(1, len(a)):
                summ += dic[a[i]]
                # print(dic[a[i]])
            a.append(num)
        else:
            for i in range(1, len(a)):
                summ += dic[a[i]]
            # print(a)
        max_num = max(max_num, summ)
        return
    for j in range(n):
        if visit[j] == 0:
            visit[j] = 1
            a.append(backpack[j][0])
            # print(a)
            dfs()
            a.pop()
            visit[j] = 0


# ６　４　３　５
# １３　８　６　１２


dfs()

print(max_num)
