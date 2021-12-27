"""
프로그래머스 타겟 넘버
BFS 형식으로 풀이
"""
from collections import deque


def solution(numbers, target):
    need_visit = deque()

    # 초기 값 (+/-) 두 개 삽입
    need_visit.append([numbers[0], 0])
    need_visit.append([-numbers[0], 0])
    num_len = len(numbers)
    count = 0
    while need_visit:
        value, idx = need_visit.popleft()
        idx += 1

        # 전체 숫자의 개수만큼 수행
        if idx < num_len:
            need_visit.append([value + numbers[idx], idx])
            need_visit.append([value - numbers[idx], idx])
        # 전체 숫자 연산 완료 후
        else:
            # 값이 타겟과 같으면
            if value == target:
                count += 1

    return count
