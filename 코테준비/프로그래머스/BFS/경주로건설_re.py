from collections import deque


def solution(board):
    def bfs(s):
        N = len(board)
        dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 왼오위아래
        visit = [[987654321 for _ in range(N)] for _ in range(N)]

        visit[0][0] = 0
        que = deque()
        que.append(s)
        while que:
            x, y, dd, count = que.popleft()

            for d in dire:
                d_x, d_y = d
                now_x, now_y = (d_x + x), (d_y + y)

                if 0 <= now_x < N and 0 <= now_y < N and board[now_x][now_y] == 0:
                    pre_x, pre_y = dd
                    count1 = count
                    if abs(abs(d_x) - abs(pre_x)) + abs(abs(d_y) - abs(pre_y)) == 0:
                        count1 = count + 100
                    elif abs(abs(d_x) - abs(pre_x)) + abs(abs(d_y) - abs(pre_y)) == 2:
                        count1 = count + 600
                    if count1 < visit[now_x][now_y]:
                        visit[now_x][now_y] = count1
                        que.append([now_x, now_y, d, count1])

        return visit[-1][-1]

    return min(bfs([0, 0, [1, 0], 0]), bfs([0, 0, [0, 1], 0]))


board = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]
print(solution(board))
