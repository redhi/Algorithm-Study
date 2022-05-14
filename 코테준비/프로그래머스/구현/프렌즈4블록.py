def solution(m, n, board):
    answer = 0
    new = []

    for i in range(len(board)):
        new.append(list(board[i]))

    while True:
        pass_list = []
        for i in range(m):
            for j in range(n):
                if 0 <= i + 1 < m and 0 <= j + 1 < n:
                    a, b, c, d = (
                        new[i][j],
                        new[i][j + 1],
                        new[i + 1][j],
                        new[i + 1][j + 1],
                    )
                    s = a + b + c + d
                    if s.count(a) == 4 and a != "0":
                        pass_list.extend(
                            [[i, j], [i, j + 1], [i + 1, j], [i + 1, j + 1]]
                        )

        pass_list = list(set(map(tuple, pass_list)))

        for i in range(len(pass_list)):
            x, y = pass_list[i]
            new[x][y] = "0"

        count = 0
        for j in range(n):
            r_str = ""
            for i in range(m):
                r_str += new[i][j]
            while r_str.count("0") > 0:
                r_str = r_str.replace("0", "")

            count += m - len(r_str)
            r_str = (m - len(r_str)) * "0" + r_str
            for k in range(len(r_str)):
                new[k][j] = r_str[k]
        print(new)
        if len(pass_list) == 0:
            answer = count
            break

    return answer


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))
