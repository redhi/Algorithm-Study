def solution(n):
    answer = []
    graph = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            print(i, j)
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            graph[x][y] = num
            print(graph)
            num += 1
    for i in graph:
        for j in i:
            if j:
                answer.append(j)

    return answer


n = 4
print(solution(n))
