"""
프로그래머스 등굣길
"""


def solution(m, n, puddles):
    answer = 0
    town = [[1 for _ in range(m)] for _ in range(n)]
    town[0][0] = 0
    town[n - 1][m - 1] = 0
    for p in puddles:
        i, j = p[0], p[1]
        town[i - 1][j - 1] = 101
  
    for i in range(len(town)):  # i - m
        for j in range(len(town[i])):  # j - n
            # print(i, j)
            if i == 0 and j == 0:
                pass
            elif j == 0:
                # town[i][j] = town[i - 1][j]
                pass
            elif i == 0:
                # town[i][j] = town[i][j - 1]
                pass
            else:
                top = town[i - 1][j]
                left = town[i][j - 1]
                if town[i][j] == 101:
                    pass
                elif top == 101:
                    town[i][j] = left
                elif left == 101:
                    town[i][j] = top
                elif top == 101 and left == 101:
                    town[i][j] = 0
                else:
                    # print(i, j, left, top)
                    town[i][j] = left + top
    print(town)
    answer = town[n - 1][m - 1]
    return answer


m = 4
n = 3
puddles = [[1, 2], [2, 2]]
solution(m, n, puddles)
