def is_right(u):
    stack = [u[0]]
    for i in range(1, len(u)):
        if stack:
            if stack[-1] == "(" and u[i] == ")":
                stack.pop()
            else:
                stack.append(u[i])
        else:
            stack.append(u[i])
    if stack:
        return False
    return True


def dfs(p):
    if p == "":
        return ""
    a_type, b_type, idx = 0, 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            a_type += 1
        else:
            b_type += 1
        if a_type == b_type:
            idx = i + 1
            break
    u = p[:idx]
    v = p[idx:]

    if is_right(u):
        return u + dfs(v)
    if not is_right(u):
        s = "(" + dfs(v) + ")"
        nn = ""
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                nn += ")"
            else:
                nn += "("
        return s + nn


def solution(p):

    return dfs(p)


p = "(()())()"

print(solution(p))
