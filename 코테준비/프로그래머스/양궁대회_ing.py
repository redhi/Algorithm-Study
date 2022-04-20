import copy
from collections import deque


def cmp(info, arr):
    score_p = 0
    score_l = 0
    # print(info, arr)
    for i in range(11):
        if info[i] == 0 and arr[i] == 0:
            continue
        if info[i] == arr[i]:
            score_p += 10 - i
        elif info[i] > arr[i]:
            score_p += 10 - i
        else:
            score_l += 10 - i
    # print(score_l, score_p)
    if score_l > score_p:
        return score_l
    return False


def solution(n, info):
    answer = []
    que = deque()
    win_max = 0
    count = 0
    a = [0] * 11

    que.append([a, 0])
    while que:
        aa, idx = que.popleft()
        if sum(aa) == n:
            value = cmp(info, aa)
            if value != False:
                win_max = max(win_max, value)
                answer.append(aa)
            continue
        elif sum(aa) > n:
            continue
        elif idx == 10:
            tmp = aa.copy()
            tmp[idx] = n - sum(tmp)
            que.append([tmp, -1])
        else:
            tmp = aa.copy()
            tmp[idx] = info[idx] + 1
            idx += 1
            que.append([tmp, idx])
            tmp2 = aa.copy()
            tmp2[idx] = 0
            que.append([tmp2, idx])
    # print(answer)

    real_an = []
    # print(len(answer))
    answer = set(list(map(tuple, answer)))
    answer = list(map(list, answer))
    # print(answer)
    for i in range(len(answer)):
        value = cmp(info, answer[i])
        if value == win_max:
            real_an.append(answer[i])
        # print(real_an)
        if real_an:
            #     real_an.sort()
            # print(real_an)
            return real_an[-1]
    return [-1]


n = 5
# n = 9
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

# info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))
