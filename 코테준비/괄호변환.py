def solution(p):
    answer = ""
    answer = dfs(p)

    return answer


def sp(s):
    for i in range(2, len(s) + 1, 2):
        new = s[:i]
        new_left = new.count("(")
        new_right = new.count(")")
        if new_left == new_right:
            u = new
            v = s[i:]
            u_v = [u, v]
            return u_v


def is_right(ss):
    stack = []
    s_dict = {"(": ")"}
    stack.append(ss[0])
    for i in range(1, len(ss)):
        if stack:
            if s_dict.get(stack[-1]) == ss[i]:
                stack.pop()
            else:
                stack.append(ss[i])
        else:
            stack.append(ss[i])

    if not stack:
        return True
    return False


def change(u):
    new_str = ""
    s_dict = {"(": ")", ")": "("}

    if len(u) == 2:
        return ""
    else:
        new_u = u[1:-1]
        for i in range(len(new_u)):
            new_str += s_dict.get(new_u[i])

        return new_str


def dfs(ss):

    if ss == "":
        return ""
    u, v = sp(ss)

    right_flag = is_right(u)
    if right_flag:
        return u + dfs(v)
    if not right_flag:
        return "(" + dfs(v) + ")" + change(u)


p = "(()())()"
p = ")("
p = "()))((()"
print(solution(p))
