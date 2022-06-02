def solution(n, build_frame):
    answer = [[]]
    arr = [[0 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]
    for build in build_frame:
        x, y, a, b = build  # a: 0기둥 1보, b: 0삭제 1설치

    return answer


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
print(solution(n, build_frame))
# 000
# 000
# 000
# 1111111
# 1010101
# 1111111
# 1010101
# 1111111
# 1010101
# 1111111
# 7 7
# 2n+1
