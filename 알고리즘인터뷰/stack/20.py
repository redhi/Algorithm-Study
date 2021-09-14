'''
20. 유효한 괄호
'''


def vaild(strs):
    stack = []
    dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for s in strs:
        if s not in dict:
            stack.append(s)
        elif dict[s] != stack.pop() or not stack:
            return False
    return True
