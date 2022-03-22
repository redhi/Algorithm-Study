"""
프로그래머스 네트워크
"""

from collections import deque


def solution(n, computers):
    answer = 0
    feild = [[] for _ in range(len(computers))]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][j] == 1 and i != j:
                feild[i].append(j)

    que = deque()
    visited = [0] * (n)

    for i in range(n):
        if visited[i] == 0:
            que.append(feild[i])
            visited[i] = 1
            while que:
                nodes = que.popleft()
                for i in range(len(nodes)):
                    if visited[nodes[i]] == 0:
                        que.append(feild[nodes[i]])
                        visited[nodes[i]] = 1
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
