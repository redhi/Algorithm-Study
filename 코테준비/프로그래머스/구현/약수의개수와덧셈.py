def check(num):
    s = set()
    for i in range(1, (num // 2) + 2):
        if num % i == 0:
            s.add(i)
            s.add(num // i)

    return len(s)


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if check(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


left = 13
right = 17
print(solution(left, right))
