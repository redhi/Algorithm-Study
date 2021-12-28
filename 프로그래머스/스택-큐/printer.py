'''
프로그래머스 프린터
'''
from collections import deque


def solution(priorities, location):
    queue = deque()
    print_list = []

    count = 0
    for p in priorities:
        if count == location:
            queue.append((p, True))
        else:
            queue.append((p, False))
        count += 1

    while queue:
        first, location = queue.popleft()
        
        # 남은 값중에 가장 큰 값 찾기
        m = sorted(queue, key=lambda x: x[0], reverse=True)
        if not len(m) == 0:
            # 추출한 값이 최대면
            if first >= m[0][0]:
                # 출력 리스트에 삽입
                print_list.append((first, location))
            else:
                # 최대가 아니면 큐 마지막에 삽입
                queue.append((first, location))
        else:
            print_list.append((first, location))

    for i in range(len(print_list)):
        if print_list[i][1] == True:
            return i + 1
