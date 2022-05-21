def solution(places):
    answer = []
    direction = [
        [[2, 0], [1, 0]],
        [[-2, 0], [-1, 0]],
        [[0, 2], [0, 1]],
        [[0, -2], [0, -1]],
        [[1, 1], [1, 0, 0, 1]],
        [[1, -1], [1, 0, 0, -1]],
        [[-1, 1], [-1, 0, 0, 1]],
        [[-1, -1], [-1, 0, 0, -1]],
        [[1, 0], []],
        [[-1, 0], []],
        [[0, 1], []],
        [[0, -1], []],
    ]
    graph = [[[] for _ in range(5)] for _ in range(5)]
    for p in range(len(places)):
        for i in range(len(places[p])):
            row = list(places[p][i])
            graph[p][i].extend(row)

    for p in range(len(graph)):
        is_wrong = False
        for i in range(len(graph[p])):
            if is_wrong:
                break
            for j in range(len(graph[i])):
                if is_wrong:
                    break
                for d in range(len(direction)):
                    if is_wrong:
                        break
                    check_i = direction[d][0][0] + i
                    check_j = direction[d][0][1] + j
                    if graph[p][i][j] == "P":
                        if 0 <= check_i < 5 and 0 <= check_j < 5:
                            if graph[p][check_i][check_j] == "P":
                                if direction[d][1] == []:
                                    is_wrong = True
                                    break
                                for k in range(0, len(direction[d][1]), 2):
                                    now_i = i + direction[d][1][k]
                                    now_j = j + direction[d][1][k + 1]
                                    if graph[p][now_i][now_j] != "X":
                                        is_wrong = True
                                        break

        if is_wrong:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [
    ["PPOOP", "OXXOX", "OPXPX", "OOPOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]
print(solution(places))
