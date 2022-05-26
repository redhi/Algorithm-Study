# 카드 구매하기
import sys

input = sys.stdin.readline

N = int(input())

pay_list = list(map(int, input().split()))
pay = []
for i in range(len(pay_list)):
    pay.append([i + 1, pay_list[i]])

pp = []
answer = 0


def dfs(count):
    global answer
    if count >= N:
        if count == N:
            answer = max(answer, sum(pp))
        return
    count1 = 0
    for p in pay:
        idx, money = p
        pp.append(money)
        count1 = count + idx
        dfs(count1)
        count1 = count - idx
        pp.pop()


dfs(0)
print(answer)
