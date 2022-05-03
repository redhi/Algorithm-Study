def solution(s):
    dic = {"(": ")"}
    stack = []
    for ss in s:
        if stack:
            if dic.get(stack[-1]) == ss:
                stack.pop()
            else:
                stack.append(ss)

        else:
            stack.append(ss)

    if stack:
        return False

    return True


s = "()()"
s = "(())()"
s = ")()("
print(solution(s))
