from collections import deque


def solution(priorities, location):
    answer = 0
    que = deque()
    for i in range(len(priorities)):
        que.append([priorities[i], i])
    while que:
        p, loca = que.popleft()
        new = sorted(que, reverse=True)
        if not new:
            answer += 1
            return answer
        if new[0][0] <= p:
            answer += 1
            if location == loca:

                return answer
        else:
            que.append([p, loca])
    return answer


priorities = [1]
location = 0
print(solution(priorities, location))
