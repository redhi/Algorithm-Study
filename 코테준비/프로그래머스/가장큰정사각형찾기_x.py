import math


def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                count = 1
                now_j = j
                while board[i][now_j] == 1:
                    if 0 <= now_j + 1 < len(board[i]):
                        now_j += 1
                        count += 1
                        now_i_ran = i + count
                        if int(math.sqrt(answer)) < count:
                            is_wrong = False
                            if now_i_ran <= len(board):
                                is_wrong = False
                                for x in range(i, now_i_ran):
                                    if is_wrong:
                                        break
                                    for y in range(j, now_j + 1):
                                        if board[x][y] != 1:
                                            is_wrong = True
                                            break
                                if not is_wrong:
                                    answer = max(answer, count ** 2)
                    else:
                        break

    return answer


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))
