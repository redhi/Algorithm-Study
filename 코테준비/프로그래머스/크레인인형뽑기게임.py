def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    for m in moves:
        for i in range(n):
            if board[i][m - 1] != 0:
                if stack:
                    if stack[-1] == board[i][m - 1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[i][m - 1])
                else:
                    stack.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
