def solution(dirs):
    dirs = list(dirs)
    answer = 0
    i, j = 0, 0
    root = set()

    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for k in range(len(dirs)):
        if dirs[k] == "U":
            dir = direction[0]
        if dirs[k] == "D":
            dir = direction[1]
        if dirs[k] == "R":
            dir = direction[2]
        if dirs[k] == "L":
            dir = direction[3]
        x = dir[0]
        y = dir[1]
        nw_i = i + x
        nw_j = j + y
        if -5 <= nw_i <= 5 and -5 <= nw_j <= 5:
            root.add((i, j, nw_i, nw_j))
            root.add((nw_i, nw_j, i, j))
            i = nw_i
            j = nw_j

    answer = len(root) // 2

    return answer


# dirs = "ULURRDLLU"
dirs = "DDDDUD"
answer = 7
print(solution(dirs))
