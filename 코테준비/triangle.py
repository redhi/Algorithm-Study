"""
프로그래머스 정수 삼각형
"""

from collections import deque


def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    answer = max(triangle[-1])
    print(answer)
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

solution(triangle)

# from collections import deque
# import copy

# def solution(triangle):
#     tri_len = len(triangle)
#     # tri = [[0] * i for i in range(1, tri_len + 1)]
#     tri = copy.deepcopy(triangle)
#     answer = 0
#     que = deque()
#     que.append([1, 0, triangle[0][0]])
#     que.append([1, 1, triangle[0][0]])
#     if tri_len == 1:
#         answer = triangle[0]
#         return answer
#     while que:
#         i, j, value = que.popleft()

#         tri[i][j] = max(triangle[i][j] + value, tri[i][j])

#         if i < tri_len - 1:
#             # 왼쪽 i+1, j
#             que.append([i + 1, j, tri[i][j]])
#             # 오른쪽 i+1, j+1
#             que.append([i + 1, j + 1, tri[i][j]])

#     answer = max(tri[-1])

#     return answer
