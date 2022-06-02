from collections import deque


def count_func(arr, type):
    num = 0
    for i in range(len(arr)):
        if type == "key":
            num += arr[i].count(1)
        else:
            num += arr[i].count(0)
    return num


def check(key, lock):
    key_arr = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                key_arr.append((i, j))
    is_break = False
    for i in range(len(lock)):
        if is_break:
            break
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                if not (i, j) in key_arr:
                    is_break = True

    if is_break:
        return False
    else:
        return True


def rotate(arr):
    new = list(map(list, zip(*arr[::-1])))
    return new


def move(arr, type):
    if type == "up":
        for i in range(1, len(arr)):
            for j in range(len(arr[i])):
                arr[i - 1][j] = arr[i][j]
                if len(arr) == i + 1:
                    arr[i][j] = 0
    elif type == "down":
        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr[i])):
                arr[i][j] = arr[i - 1][j]
                if 1 == i:
                    arr[i - 1][j] = 0
    elif type == "left":
        temp_arr = list(map(list, zip(*arr)))
        for i in range(1, len(temp_arr)):
            for j in range(len(temp_arr[i])):
                temp_arr[i - 1][j] = temp_arr[i][j]
                if len(temp_arr) == i + 1:
                    temp_arr[i][j] = 0
        arr = list(map(list, zip(*temp_arr)))
    else:
        temp_arr = list(map(list, zip(*arr)))
        for i in range(len(temp_arr) - 1, 0, -1):
            for j in range(len(temp_arr[i])):
                temp_arr[i][j] = temp_arr[i - 1][j]
                if 1 == i:
                    temp_arr[i - 1][j] = 0
        arr = list(map(list, zip(*temp_arr)))

    return arr


def solution(key, lock):
    lock_num = count_func(lock, "lock")

    que = deque()
    que.append(key)

    is_true = False
    while que:
        now = que.popleft()
        if lock_num > count_func(now, "key"):
            continue
        if check(now, lock):
            is_true = True
            break

        r_now = rotate(now)
        u_now = move(now, "up")
        d_now = move(now, "down")
        l_now = move(now, "left")
        ri_now = move(now, "right")
        change_now = [r_now, u_now, d_now, l_now, ri_now]
        for c_now in change_now:
            if lock_num <= count_func(c_now, "key"):
                que.append(c_now)
        # print(que)

    return is_true


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
