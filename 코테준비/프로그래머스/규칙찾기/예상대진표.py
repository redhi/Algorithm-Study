def check(a, b):
    if a % 2 == 0:
        a //= 2
    else:
        a += 1
        a //= 2
    if b % 2 == 0:
        b //= 2
    else:
        b += 1
        b //= 2
    if abs(b - a) != 0:
        return True
    return False


def solution(n, a, b):
    answer = 0
    while check(a, b):
        if a % 2 == 0:
            a //= 2
        else:
            a += 1
            a //= 2
        if b % 2 == 0:
            b //= 2
        else:
            b += 1
            b //= 2
        answer += 1

    if abs(a - b) == 1:
        answer += 1

    return answer


n = 8
a = 4
b = 5
print(solution(n, a, b))
