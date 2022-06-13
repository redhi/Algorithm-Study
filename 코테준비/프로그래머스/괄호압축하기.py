import copy
from collections import deque


def solution(s):
    answer = 0
    s = list(s)
    stack = deque(s)

    for i in range(len(s)):
        ro_stack = copy.deepcopy(stack)
        ro_stack.rotate(-i)
        result = is_right(ro_stack)
        answer += result

    return answer


def is_right(s):
    s = list(s)
    s_dict = {"(": ")", "[": "]", "{": "}"}
    new_stack = []
    new_stack.append(s[0])

    for i in range(1, len(s)):
        if new_stack:
            if s_dict.get(new_stack[-1]) == s[i]:
                new_stack.pop()
            else:
                new_stack.append(s[i])
        else:
            new_stack.append(s[i])

    if not new_stack:
        return 1
    else:
        return 0


s = "[](){}"
s = "}]()[{"
s = "[)(]"
print(solution(s))
