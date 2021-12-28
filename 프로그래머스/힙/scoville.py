'''
프로그래머스 더 맵게
'''
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        one = heapq.heappop(scoville)
        if one >= K:
            return answer
        two = heapq.heappop(scoville)
        answer += 1
        new = one + (two * 2)

        heapq.heappush(scoville, new)

    # 남은 원소가 1일때 K보다 작으면 -1
    if len(scoville) == 1:
        one = heapq.heappop(scoville)
        if one < K:
            answer = -1

    return answer
