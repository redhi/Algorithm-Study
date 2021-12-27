"""
프로그래머스 네트워크 
DFS 형식으로 풀이(재귀 x)
"""
from collections import deque


def solution(n, computers):
    answer, idx = 0, 0
    queue = deque()
    # 초기 방문 큐 설정
    visited = [False for _ in range(n)]

    # 전체 방문 전까지 반복
    while visited.count(False) != 0:
        # 가장 첫 번째 방문하지 않은 인덱스 찾기
        idx = visited.index(False)
        queue.append(idx)

        while queue:
            # 맨 끝의 인덱스(노드) 반환
            idx = queue.pop()
            visited[idx] = True

            for i in range(0, n):
                # 각 노드(인덱스)간 연결되어 있고 방문하지 않은 노드(인덱스)라면
                if computers[idx][i] == 1 and visited[i] == False:
                    # 방문처리 후 큐에 삽입
                    visited[i] = True
                    queue.append(i)
        
        # 각 노드에 연결된 모든 노드 방문끝낸 후 answer 1 증가
        answer += 1

    return answer
