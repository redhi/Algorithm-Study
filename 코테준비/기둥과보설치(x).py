from distutils.command.build import build


def solution(n, build_frame):
    answer = [[]]
    list_arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    print(list_arr[0][1])
    print(list_arr)
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        # 설치
        is_ok = check(list_arr, build_frame[i], n)
        print(is_ok)

        # 기둥
        if a == 0 and b == 1:
            if is_ok:
                list_arr[x][y] = 1
                list_arr[x][y + 1] = 1
        # 보
        if a == 1 and b == 1:
            if is_ok:
                print("보임", x, y)
                list_arr[x][y] = 1
                list_arr[x + 1][y] = 1
                print(list_arr)
        # 삭제
        if a == 0 and b == 0:
            if is_ok:
                list_arr[x][y] = 0
                list_arr[x][y + 1] = 0
        if a == 1 and b == 0:
            if is_ok:
                list_arr[x][y] = 0
                list_arr[x + 1][y] = 0
    print(list_arr)

    return answer


def check(list_arr, build, n):
    x, y, a, b = build
    print(x, y, a, b)
    if a == 0 and b == 1:
        if y == 0:
            return True
        else:
            if list_arr[x][y] == 1:
                return True
            else:
                return False
    if a == 1 and b == 1:
        if y == 0:
            return False
        else:
            if list_arr[x][y] == 1 or list_arr[x + 1][y] == 1:
                return True
            else:
                return False
    # if a == 0 and b == 0:
    #     if y + 1 > n or y + 2 > n or x + 1 > n or x - 1 < 0 or y - 2 < n or y - 1 < n:
    #         pass
    #     else:
    #         if list_arr[x][y + 1] == 1 and list_arr[x][y + 2] == 1:
    #             return True
    #         elif list_arr[x + 1][y + 1] == 1 and list_arr[x + 1][y] == 1:
    #             return True
    #         elif list_arr[x + 1][y + 1] == 1 and list_arr[x + 1][y] != 1:
    #             return False
    #         elif list_arr[x - 1][y + 1] == 1 and list_arr[x - 1][y] == 1:
    #             return True

    if a == 1 and b == 0:
        if (list_arr[x - 1][y - 1] == 1 and list_arr[x - 1][y] == 1) and (
            list_arr[x + 1][y - 1] == 1 and list_arr[x + 1][y] == 1
        ):
            return True
        else:
            return False


n = 5
build_frame = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
]
build_frame = [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1],
]

print(solution(n, build_frame))
