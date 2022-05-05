from collections import deque


def can(cur1, cur2, board):
    Y, X = 0, 1
    cand = []
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    N = len(board)
    for dy, dx in dire:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        print(nxt1[Y], nxt1[X], " ", nxt2[Y], nxt2[X])
        if (
            0 <= nxt1[Y] < N
            and 0 <= nxt1[X] < N
            and 0 <= nxt2[Y] < N
            and 0 <= nxt2[X] < N
        ):
            if board[nxt1[Y]][nxt1[X]] == 0 and board[nxt2[Y]][nxt2[X]] == 0:
                cand.append((nxt1, nxt2))
            # 가로
            if cur1[Y] == cur2[Y]:
                UP, DOWN = -1, 1
                for d in [UP, DOWN]:
                    if 0 <= cur1[Y] + d < N and 0 <= cur2[Y] + d < N:
                        if (
                            board[cur1[Y] + d][cur1[X]] == 0
                            and board[cur2[Y] + d][cur2[X]] == 0
                        ):
                            cand.append((cur1, (cur1[Y] + d, cur1[X])))
                            cand.append((cur2, (cur2[Y] + d, cur2[X])))
            else:
                LEFT, RIGHT = -1, 1
                for d in [LEFT, RIGHT]:
                    if 0 <= cur1[X] + d < N and 0 <= cur2[X] + d < N:
                        if (
                            board[cur1[Y]][cur1[X] + d] == 0
                            and board[cur2[Y]][cur2[X] + d] == 0
                        ):
                            cand.append((cur1, (cur1[Y], cur1[X] + d)))
                            cand.append((cur2, (cur2[Y], cur2[X] + d)))
    return cand


def solution(board):
    N = len(board)
    now = [(0, 0), (0, 1), 0]
    visit = set([((0, 0), (0, 1))])

    que = deque()
    que.append(now)
    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N - 1, N - 1) or cur2 == (N - 1, N - 1):
            return count
        for nxt in can(cur1, cur2, board):
            if nxt not in visit:
                que.append((*nxt, count + 1))
                visit.add(nxt)


board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
print(solution(board))
