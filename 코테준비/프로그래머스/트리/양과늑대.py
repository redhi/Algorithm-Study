a = []
from collections import defaultdict, deque

max_sheep = 0


def dfs(graph, node, visit, sheep, wolf, info):
    global max_sheep
    print(node, sheep, wolf, visit)
    if sheep <= wolf:
        # print(sheep, wolf)
        # dfs(graph,node, visit,)
        wolf -= 1
        visit[node] = 0
        print("으아아", visit, node, sheep, wolf)
        # dfs(graph, node, visit, sheep, wolf, info)
        return
    if len(graph[node]) == 1:
        if visit[graph[node][0]] == 1:
            visit[node] = 1

    for i in range(len(graph[node])):
        next_node = graph[node][i]
        if visit[next_node] == 0:
            if info[next_node] == 0:
                sheep += 1
            else:
                wolf += 1
            visit[next_node] = 1
            max_sheep = max(max_sheep, sheep)
            print("들어간 애", next_node, sheep, wolf)
            a.append(next_node)
            print(a)
            dfs(graph, next_node, visit, sheep, wolf, info)
            visit[next_node] = 0
            # if info[next_node] == 0:
            #     sheep -= 1
            # else:
            #     wolf -= 1
    # print(sheep, wolf)


def solution(info, edges):
    global max_sheep
    answer = 0
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    print(graph)
    visit = [0 for _ in range(len(info))]
    visit[0] = 1
    dfs(graph, 0, visit, 1, 0, info)
    print("냐", max_sheep)
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
