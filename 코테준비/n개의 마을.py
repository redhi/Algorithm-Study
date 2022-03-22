import heapq


def solution(N, road, K):
    answer = 0
    heap = []
    graph = [[] for _ in range(N + 1)]
    for i in road:
        graph[i[0]].append([i[2], i[1]])
        graph[i[1]].append([i[2], i[0]])

    d = [100000000] * (N + 1)
    d[1] = 0
    heapq.heappush(heap, [0, 1])

    while heap:
        wei, node = heapq.heappop(heap)
        if d[node] < wei:
            continue
        for i in range(len(graph[node])):
            next = graph[node][i][1]
            if wei + graph[node][i][0] < d[next]:
                d[next] = wei + graph[node][i][0]
                heapq.heappush(heap, [wei + graph[node][i][0], graph[node][i][1]])

    for i in range(len(d)):
        if d[i] <= K:
            answer += 1
 
    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
solution(N, road, K)
