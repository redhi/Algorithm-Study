from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    d = [2000001] * (n + 1)
    visit = [0] * (n + 1)
    d[1] = 0
    for i in edge:
        graph[i[0]].append([1, i[1]])
        graph[i[1]].append([1, i[0]])

    que = deque()
    que.append(1)
    while que:
        node = que.popleft()
        for i in range(len(graph[node])):
            link_wei, next_node = graph[node][i]
            if visit[next_node] == 0:
                d[next_node] = min(d[node] + link_wei, d[next_node])
                que.append(next_node)
                visit[next_node] = 1

    for i in range(len(d)):
        if d[i] == 2000001:
            d[i] = 0

    max_d = max(d)
    answer = d.count(max_d)
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
