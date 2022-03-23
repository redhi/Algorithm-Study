def solution(grid):
    answer = []
    graph = []
    for i in range(len(grid)):
        s = list(grid[i])
        graph.append(s)
    route = set()
    dfs(0, 0, 1, 0, graph, 0, route)

    print(graph)
    return answer


def dfs(b_i, b_j, a_i, a_j, graph, count, route):
    type = graph[a_i][a_j]
    mini_route = [b_i, b_j, a_i, a_j]
    route2 = list(route)
    if mini_route in route2:
        return count
    else:
        print(route)
        route.add((b_i, b_j, a_i, a_j))
    if type == "S":
        if a_i - b_i == 1:
            aa_i = check(a_i + 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_j - b_j == 1:
            aa_j = check(a_j + 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)
        if a_i - b_i == -1:
            aa_i = check(a_i - 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_j - b_j == -1:
            aa_j = check(a_j - 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)
    if type == "L":
        if a_j - b_j == 1:
            aa_i = check(a_i - 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_j - b_j == -1:
            aa_i = check(a_i + 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_i - b_i == 1:
            aa_j = check(a_j - 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)
        if a_i - b_i == -1:
            aa_j = check(a_j + 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)
    if type == "R":
        if a_j - b_j == 1:
            aa_i = check(a_i + 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_j - b_j == -1:
            aa_i = check(a_i - 1, graph)
            dfs(a_i, a_j, aa_i, a_j, graph, count + 1, route)
        if a_i - b_i == 1:
            aa_j = check(a_j + 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)
        if a_i - b_i == -1:
            aa_j = check(a_j - 1, graph)
            dfs(a_i, a_j, a_i, aa_j, graph, count + 1, route)


def check(node, graph):
    if node >= len(graph):
        return 0
    else:
        return node


grid = ["SL", "LR"]
print(solution(grid))
