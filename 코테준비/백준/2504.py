def sol(s):
    right_dict = {")": "(", "]": "["}
    stack = []
    answer = []
    for i in range(len(s)):
        if stack:
            if right_dict.get(s[i]) == stack[-1][0]:
                if s[i] == ")" and stack[-1][1] == i - 1:
                    answer.append(2)
                    answer.append("+")
                if s[i] == ")" and stack[-1][1] != i - 1:
                    num = answer.pop()
                    answer.append(num * 2)
                if s[i] == "]" and stack[-1][1] == i - 1:
                    answer.append(3)
                    answer.append("+")
                if s[i] == "]" and stack[-1][1] != i - 1:
                    num = answer.pop()
                    answer.append(num * 3)
                stack.pop()
            else:
                stack.append([s[i], i])
        else:
            print("끝")
            if i != 0:
                answer.append("+")
            stack.append([s[i], i])
        print(stack)
        print(answer)
    if stack:
        return 0
    a = 0
    # for i in range(len(answer)):

    print(stack)


s = "(()[[]])([])"
print(sol(s))
