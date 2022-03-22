"""
프로그래머스 타켓넘버
"""

from collections import deque


def solution(numbers, target):
    answer = 0
    que = deque()
    que.append([-numbers[0], 0])
    que.append([numbers[0], 0])

    while que:
        value, i = que.popleft()

        if i + 1 < len(numbers):
            que.append([value - numbers[i + 1], i + 1])
            que.append([value + numbers[i + 1], i + 1])
        else:
            if value == target:
                answer += 1

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
