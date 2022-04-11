import math


def solution(w, h):
    g = math.gcd(w, h)

    answer = h * w - (w + h - g)
    return answer


w = 4
h = 4
print(solution(w, h))
