import math


def solution(brown, yellow):
    answer = []
    y_sqrt = int(math.sqrt(yellow)) + 1
    alt = []
    for i in range(1, y_sqrt):
        if yellow % i == 0:
            temp = [i + 2, yellow // i + 2]
            temp.sort(reverse=True)
            alt.append(temp)

    for i in range(len(alt)):
        x, y = alt[i]
        if (x * y - brown) == yellow:
            return alt[i]

    return answer


# 12 2
# 3 4
# 6 2
# 1 2
# 1+2 2+2

brown = 24
yellow = 24
print(solution(brown, yellow))
