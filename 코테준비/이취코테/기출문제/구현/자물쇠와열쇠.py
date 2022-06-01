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

                    # print(i, j)
    if is_break:
        return False
    else:
        return True


def rotate(arr):
    new = list(map(list, zip(*arr[::-1])))
    return new
    print(list(map(list, zip(*arr[::-1]))))


def move(arr, type):
    if type == "up":
        for i in range(1, len(arr)):
            for j in range(len(arr[i])):
                arr[i - 1][j] = arr[i][j]
                if len(arr) == i + 1:
                    arr[i][j] = 0
                # print("으하하", arr)
        return arr
    else:
        for i in range(1, len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = arr[i - 1][j]
                if len(arr) == i + 1:
                    arr[i][j] = 0
                # print("으하하", arr)
        return arr


def solution(key, lock):
    answer = True
    print(check(key, lock))
    new = rotate(key)
    print(new)
    print(move(new, "up"))

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
