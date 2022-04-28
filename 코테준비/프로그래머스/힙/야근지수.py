import heapq


def solution(n, works):
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    if sum(works) <= n:
        return 0
    answer = 0
    while n > 0:
        a = heapq.heappop(heap)
        a = abs(a)-1
        n -= 1
        heapq.heappush(heap, -a)

    for w in heap:
        answer += w ** 2
    return answer


n = 3
works = [1, 1]
print(solution(n, works))
