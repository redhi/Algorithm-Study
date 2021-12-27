"""
프로그래머스 기능개발
"""
import copy
import math
from collections import deque


def solution(progresses, speeds):
    queue = deque()
    answer = []

    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        queue.append(day)

    while queue:
        count = 1
        first = queue.popleft()
        # 아래서 for문을 돌때 원본에 손상이 안가게
        orgin = copy.deepcopy(queue)

        for q in orgin:
            # 뒤에 날짜가 더 크면 배포 불가
            if q > first:
                break
            queue.popleft()
            count += 1
        answer.append(count)

    return answer
