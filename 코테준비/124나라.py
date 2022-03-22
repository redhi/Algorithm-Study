from sqlalchemy import true


def solution(n):
    answer = ""
    return answer


count = [[1, 0], [2, 0], [4, 0]]
n = 1
a = []
visit = [0, 0, 0]
num = [1, 2, 4]
print(visit)

count = 0


def dfs(start, n):
    global count

    if count == n:
        print(a)
        return

    for i in range(start % 3, 3):
        a.append(num[i])
        count += 1
        dfs(i + 1, n)
        a.pop()


dfs(0, 2)
solution(n)
# 8진법
# 01234567
# 124
# 124
# 1 1
# 2 2
# 3 4
# 1 2 4 0 0 0
# 1 1 1
