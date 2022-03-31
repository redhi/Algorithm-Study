from itertools import combinations


def solution(relation):
    answer = 0
    column_len = len(relation[0])
    col = [[] for _ in range(column_len)]
    for i in range(len(relation)):
        for j in range(len(relation[i])):
            col[j].append(relation[i][j])

    right = []

    column = [i + 1 for i in range(column_len)]

    choice = []
    for i in range(column_len):
        l = list(map(list, combinations(column, i + 1)))
        choice.append(l)

    for i in range(len(choice)):
        for j in range(len(choice[i])):
            idx_arr = [[] for _ in range(len(relation))]
            for k in range(len(choice[i][j])):

                idx = choice[i][j][k] - 1
                now_col = col[choice[i][j][k] - 1]
                for z in range(len(now_col)):
                    now_str = idx_arr[z]
                    if now_str == []:
                        now_str = ""

                    now_str += relation[z][idx]
                    idx_arr[z] = now_str

            before_len = len(idx_arr)
            idx_arr = set(idx_arr)
            after_len = len(idx_arr)
            if before_len == after_len:
                if len(right) == 0:
                    right.append(choice[i][j])
                is_False = False
                for r in range(len(right)):
                    count = 0
                    for rr in range(len(choice[i][j])):
                        if count < len(right[r]):
                            if choice[i][j][rr] in right[r]:
                                count += 1
                        else:
                            is_False = True
                            break
                    if count == len(right[r]):
                        is_False = True

                if not is_False:
                    right.append(choice[i][j])

    answer = len(right)

    return answer


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]
print(solution(relation))
