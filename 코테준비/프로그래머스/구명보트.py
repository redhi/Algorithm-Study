from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        w = people.popleft()

        is_two = False
        for i in range(len(people) - 1, -1, -1):
            if people[i] + w <= limit:
                people.pop()
                answer += 1
                is_two = True
                break
            else:
                people.pop()
                answer += 1
        if not is_two:
            answer += 1

    return answer


people = [20, 20, 10, 20, 30, 80, 100, 80]
limit = 100
print(solution(people, limit))
