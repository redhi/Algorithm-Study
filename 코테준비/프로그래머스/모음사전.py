a = []
total = []


def dfs(n, arr):
    if len(a) == n:
        str_a = "".join(a)
        total.append(str_a)
        return
    for i in range(len(arr)):
        a.append(arr[i])
        dfs(n, arr)
        a.pop()


def solution(word):
    answer = 0
    arr = ["A", "E", "I", "O", "U"]

    for i in range(1, 6):
        dfs(i, arr)
    total.sort()
    answer = total.index(word) + 1
    return answer


word = "AAAAE"
print(solution(word))
