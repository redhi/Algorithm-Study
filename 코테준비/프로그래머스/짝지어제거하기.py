def solution(s):
    answer = -1
    stack = []

    for i in range(len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        answer = 1
    else:
        answer = 0
    return answer
