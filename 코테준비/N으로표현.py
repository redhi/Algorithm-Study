"""
프로그래머스 N으로 표현
"""
from collections import deque


def solution(N, number):
    dp = [set([N * int("1" * i)]) for i in range(1, 9)]
    answer = 0

    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i - j - 1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        if number in dp[i]:
            # print(dp)
            return i + 1
    return -1


# def dp(N, number):

N = 5
number = 12

print(solution(N, number))
