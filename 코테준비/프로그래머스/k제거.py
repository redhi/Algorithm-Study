number = "1924"

a = []
answer = ""
lst = []


def solution(number, k):
    answer = ""
    stack = []
    left = len(number) - k

    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    for i in range(left):
        answer += stack[i]

    return answer


def dfs(num, start, k):
    global answer

    if len(a) == k:
        i = "".join(a)
        lst.append(i)
        print(lst)
        print(a)
        answer = max(lst)

        return

    for i in range(start, len(num)):
        a.append(num[i])
        dfs(num, i + 1, k)
        a.pop()


k = 2
print(solution(number, k))
