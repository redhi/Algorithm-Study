from collections import defaultdict, deque


def dfs(que, sh_cnt, wo_cnt):
    global answer
    answer = max(sh_cnt, answer)
    for _ in range(len(que)):
        node = que.popleft()
        if infos[node] == 1:
            if sh_cnt > wo_cnt + 1:
                for j in D[node]:
                    que.append(j)
                dfs(que, sh_cnt, wo_cnt + 1)
                for j in D[node]:
                    que.pop()
        else:
            for j in D[node]:
                que.append(j)
            dfs(que, sh_cnt + 1, wo_cnt)
            for j in D[node]:
                que.pop()
        que.append(node)  # 마지막에 넣어줌


def solution(info, edges):
    global answer, infos, D
    infos = info  # 양, 늑대 여부
    answer = 0
    D = defaultdict(list)  # 그래프
    que = deque()
    for i in edges:
        D[i[0]].append(i[1])
    # print(D)
    que.append(0)
    dfs(que, 0, 0)
    return answer


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [
    [0, 1],
    [1, 2],
    [1, 4],
    [0, 8],
    [8, 7],
    [9, 10],
    [9, 11],
    [4, 3],
    [6, 5],
    [4, 6],
    [8, 9],
]
print(solution(info, edges))
