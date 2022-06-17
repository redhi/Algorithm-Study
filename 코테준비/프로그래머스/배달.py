import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    heap = []
    for i in road:
        graph[i[0]].append([i[2], i[1]])
        graph[i[1]].append([i[2], i[0]])
    d = [10000002 for _ in range(N + 1)]
    heapq.heappush(heap, [0, 1])
    d[1] = 0
    while heap:
        wei, node = heapq.heappop(heap)
        for next_w, next_n in graph[node]:
            new_w = next_w + wei
            if d[next_n] < new_w:
                continue
            # if wei > new_w:
            heapq.heappush(heap, [new_w, next_n])
            d[next_n] = new_w
    # print(graph)
    # print(d)
    for i in range(1, len(d)):
        if d[i] <= K:
            answer += 1

    return answer


N = 6
road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
K = 4

print(solution(N, road, K))
