"""
프로그래머스 체육복
"""


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    visit = []
    for i in range(1, n + 1):
        if i in lost:
            visit.append(0)
        else:
            visit.append(1)

    for i in reserve:
        if i in lost:
            visit[i - 1] = 1
            continue
        if i == 1:
            if visit[i] == 0:
                visit[i] = 1
        elif i == n:
            if visit[i - 2] == 0:
                visit[i - 2] = 1
        else:
            count = 0
            if visit[i - 2] == 0:
                visit[i - 2] = 1
                count += 1
            if visit[i] == 0 and count == 0:
                visit[i] = 1

        visit[i - 1] = 1

    answer = sum(visit)
    return answer


n = 10
lost = [1, 8]
reserve = [3, 6, 10]
solution(n, lost, reserve)
solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9])

# def solution(n, lost, reserve):
#     answer = 0
#     visit = []
#     for i in range(1, n + 1):
#         if i in lost:
#             visit.append(0)
#         elif i in reserve:
#             visit.append(2)
#         else:
#             visit.append(1)
#
#     for i in reserve:
#         if i in lost:
#             visit[i - 1] = 1
#             continue
#         if i == 1:
#             if visit[i] == 0:
#                 visit[i] = 1
#         elif i == n:
#             if visit[i - 2] == 0:
#                 visit[i - 2] = 1
#         else:
#             count = 0
#             if visit[i - 2] == 0:
#                 visit[i - 2] = 1
#                 count += 1
#             if visit[i] == 0 and count == 0:
#                 visit[i] = 1
#         visit[i - 1] -= 1
#
#     answer = sum(visit)
#     return answer
