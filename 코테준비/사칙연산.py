from collections import deque


def solution(N, number):
    num_list = [set([int(str(N) * i)]) for i in range(1, 9)]

    for i in range(8):
        for j in range(i):
            for num1 in num_list[j]:
                for num2 in num_list[i - j - 1]:
                    num_list[i].add(num1 + num2)
                    num_list[i].add(num1 - num2)
                    num_list[i].add(num1 * num2)
                    if num2 != 0:
                        num_list[i].add(num1 // num2)

        if number in num_list[i]:
            return i + 1

    return -1


N = 5
number = 12

print(solution(N, number))
