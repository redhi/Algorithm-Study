"""
백준 프린터 큐
"""

import sys
from collections import deque

input = sys.stdin.readline


def print_queue(queue, N, M):

    count = 0
    visited_idx = deque([0 for _ in range(N)])
    visited_idx[M] = 1

    while queue:
        max_num = max(queue)
        node = queue[0]

        if node == max_num:
            queue.popleft()
            idx = visited_idx.popleft()
            count += 1

            if idx == 1:
                return count
        else:
            queue.append(queue.popleft())
            visited_idx.append(visited_idx.popleft())


T = int(input())

answer = deque()
for i in range(T):
    N, M = map(int, input().split())
    d_list = deque(map(int, input().split()))
    answer.append(str(print_queue(d_list, N, M)))

sys.stdin.write("\n".join(answer))
