a = []
count = 0


def dfs(i, n):
    global count
    if sum(a) >= n:
        if sum(a) == n:
            count += 1
            # print(a)
        return
    for j in range(i + 1, i + 2):
        # print(a)
        a.append(j)
        dfs(j, n)
        a.pop()


def solution(n):
    global count
    for i in range(0, n + 1):
        dfs(i, n)
    return count


n = 15
print(solution(n))
