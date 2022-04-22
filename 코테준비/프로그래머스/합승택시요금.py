import heapq


def kru(graph, nn, d):
    heap = []
    heapq.heappush(heap, [0, nn])
    d[nn] = 0
    while heap:
        value, node = heapq.heappop(heap)
        for i in range(len(graph[node])):
            next_value, next_node = graph[node][i]
            if d[next_node] > d[node] + next_value:
                d[next_node] = d[node] + next_value
                heapq.heappush(heap, [d[next_node], next_node])
            else:
                continue


def solution(n, s, a, b, fares):
    INF = 987654321
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        ss, e, f = fare
        graph[ss].append([f, e])
        graph[e].append([f, ss])

    col = [s, a, b]
    d = [[INF] * (n + 1), [INF] * (n + 1), [INF] * (n + 1)]
    for i in range(3):
        kru(graph, col[i], d[i])

    answer = INF
    for i in range(1, n + 1):
        summ = 0
        for j in range(3):
            summ += d[j][i]
        answer = min(answer, summ)

    return answer


n = 6
s = 4
a = 6
b = 2
fares = [
    [4, 1, 10],
    [3, 5, 24],
    [5, 6, 2],
    [3, 1, 41],
    [5, 1, 24],
    [4, 6, 50],
    [2, 4, 66],
    [2, 3, 22],
    [1, 6, 25],
]
print(solution(n, s, a, b, fares))
