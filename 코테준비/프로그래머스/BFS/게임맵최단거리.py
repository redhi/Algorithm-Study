from collections import deque


def solution(maps):
    answer = 0
    dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n, m = len(maps), len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    que = deque()
    que.append([[0, 0], 1])
    is_ok = False
    minn = 987654321
    
    while que:
        d, count = que.popleft()
        x, y = d
        if x == n - 1 and y == m - 1:
            is_ok = True
            minn = min(minn, count)
        
        for i in range(len(dire)):
            xx, yy = dire[i]
            now_x = x + xx
            now_y = y + yy

            if 0 <= now_x < n and 0 <= now_y < m:
                if maps[now_x][now_y] == 1 and visit[now_x][now_y] == 0:
                    visit[now_x][now_y] = 1
                    count2 = count + 1
                    que.append([[now_x, now_y], count2])
    if is_ok:
        answer = minn
    else:
        answer = -1
    return answer


maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]

print(solution(maps))
