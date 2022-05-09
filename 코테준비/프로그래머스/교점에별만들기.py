def solution(line):
    answer = []
    for i in range(len(line) - 1):
        for j in range(i, len(line)):
            for k in range(3):
                if abs(line[i][k]) == abs(line[i][k]):
                    pass
            # for num1, num2 in zip(line[i], line[j]):
            # print(num1, num2)

    return answer


# 4x=0

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
