import heapq


def solution(operations):
    heap = []
    heap_r = []
    i_count, d_count = 0, 0
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == "I":
            i_count += 1
        else:
            d_count += 1
        if i_count < d_count:
            heap, heap_r = [], []
            i_count, d_count = 0, 0
            continue
        if cmd == "I":
            heapq.heappush(heap, num)
            heapq.heappush(heap_r, -num)
        if cmd == "D":
            if num == 1:
                heapq.heappop(heap_r)
            if num == -1:
                heapq.heappop(heap)

    heap = set(heap)
    heap_r = [-i for i in heap_r]
    heap_r = set(heap_r)
    and_list = list(heap & heap_r)
    if len(and_list) == 0:
        return [0, 0]
    else:
        return [max(and_list), min(and_list)]


operations = ["I 16", "I 6", "D 1"]
operations = ["I 7", "I 5", "I -5", "D -1"]
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

print(solution(operations))
