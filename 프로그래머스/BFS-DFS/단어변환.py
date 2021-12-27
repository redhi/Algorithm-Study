"""
프로그래머스 단어변환
bfs 형식으로 풀이
"""
from collections import deque


def solution(begin, target, words):
    answer = 0
    # 단어 집합에 타켓 단어가 없으면 0 반환
    if target not in words:
        return 0

    visited = [False for _ in range(len(words))]
    answer = bfs(begin, target, words, visited)
    return answer


def bfs(begin, target, words, visited):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        node, depth = queue.popleft()
        # 타켓 단어면 깊이 반환
        if node == target:
            return depth
        for i in range(len(words)):
            # 방문한적 없으면
            if not visited[i] == True:
                dif = 0

                for w1, w2 in zip(node, words[i]):
                    if w1 != w2:
                        dif += 1

                # 현재 단어와 한글자만 다르면 큐에 삽입
                if dif == 1:
                    visited[i] = True
                    queue.append((words[i], depth + 1))
