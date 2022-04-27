def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = columns * i + j + 1

    for query in queries:
        s_y = query[0] - 1
        s_x = query[1] - 1
        e_y = query[2] - 1
        e_x = query[3] - 1

        round_arr = []

        for i in range(s_x, e_x + 1):
            round_arr.append([s_y, i, arr[s_y][i]])
        for i in range(s_y + 1, e_y + 1):
            round_arr.append([i, e_x, arr[i][e_x]])
        for i in range(e_x - 1, s_x, -1):
            round_arr.append([e_y, i, arr[e_y][i]])
        for i in range(e_y, s_y, -1):
            round_arr.append([i, s_x, arr[i][s_x]])

        min_num = 987654321
        for i in range(len(round_arr)):
            if i == len(round_arr) - 1:
                arr[round_arr[0][0]][round_arr[0][1]] = round_arr[i][2]
            else:
                arr[round_arr[i + 1][0]][round_arr[i + 1][1]] = round_arr[i][2]
            min_num = min(min_num, round_arr[i][2])

        answer.append(min_num)

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rows, columns, queries))
