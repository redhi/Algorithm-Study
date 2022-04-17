def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_num = 0
            for k in range(4):
                if j != k:
                    max_num = max(land[i - 1][k], max_num)
            land[i][j] += max_num

    answer = max(land[len(land) - 1])
    return answer


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

print(solution(land))
