from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    n = len(people)
    limit0 = limit
    count = 0
    idx = -1
    while people:
        w = people.popleft()
        idx += 1
        limit0 -= w
        count += 1
        # print(w, limit0)
        # print(count, idx, w)
        if limit0 <= 0 or count == 2:
            if limit0 < 0:
                people.appendleft(w)
                idx -= 1
            limit0 = limit
            count = 0
            answer += 1
            # print("이야", people, answer, idx)

        if n == (idx + 1) and count == 1:
            answer += 1

    return answer


people = [20, 20, 10, 20, 30, 80]
limit = 100
print(solution(people, limit))
