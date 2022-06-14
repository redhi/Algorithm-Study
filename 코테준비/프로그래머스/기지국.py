import copy
from collections import deque


def solution(n, stations, w):
    answer = 0

    left_ran = []

    e = 0
    for s in range(len(stations)):
        start = stations[s] - w
        end = stations[s] + w
        if start < 1:
            start = 1
        if end > n:
            end = n
        if s != 0:
            e = stations[s - 1] + w + 1
        else:
            e = 1

        count = 0
        # print(e, start)

        count = start - e
        if count > 0:
            left_ran.append(count)
        # print(s, len(stations), end, n)
        if s + 1 == len(stations) and end < n:
            count = n - end
            left_ran.append(count)

    # print(left_ran)
    ran = 2 * w + 1
    for i in left_ran:
        if i <= ran:
            answer += 1
        else:
            answer += (i // ran) + 1
    return answer
    # if i <= start:

    #     print(start, end)
    # # for i in range(1, len(house)):
    # #     if house[i] == 0:
    # #         pass

    # print(house)
    # house_copy = copy.deepcopy(house)
    # # for i in range(len(house)):
    # #     if house[i] == 0:
    # for i in range(1, len(house)):
    #     if house[i] == 0:
    #         que.append([i, 0])
    #     if house[i] == 1:
    #         break
    # cnt_list = []
    # while que:
    #     now_loca, cnt = que.popleft()
    #     is_t = 0
    #     print(now_loca, cnt)
    #     if now_loca >= n:
    #         print(now_loca)
    #         cnt_list.append(cnt)
    #     if house[now_loca] == 0:
    #         next_w = now_loca + w + 1
    #         que.append([next_w, cnt + 1])
    #     else:
    #         start = 0

    #         for i in range(now_loca, len(house)):
    #             if house[i] == 0:
    #                 start = i
    #                 is_t = 1
    #                 break
    #         if is_t == 1:
    #             for j in range(start, start + w + 1):
    #                 print("j", j, start, start + w)
    #                 next_w = j + w + 1
    #                 que.append([next_w, cnt + 1])
    # print(cnt_list)


N = 16
stations = [8, 9]
W = 2
print(solution(N, stations, W))
