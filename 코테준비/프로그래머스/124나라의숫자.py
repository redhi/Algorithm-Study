from collections import deque


def solution(n):
    answer = ""
    result = deque()
    num1 = n - 1
    num2 = 0
    while num1 >= 0:
        num2 = num1 % 3
        num1 //= 3

        if num2 == 0:
            result.appendleft(1)
        if num2 == 1:
            result.appendleft(2)
        if num2 == 2:
            result.appendleft(4)
        num1 -= 1

    answer = "".join(map(str, result))
    return answer


n = 35

print(solution(n))
# 1 2 4
# 11 12 14
# 21 22 24
#
