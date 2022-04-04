def sol(s):
    right_dict = {")": "(", "]": "["}
    stack = []
    answer = []

    for i in range(len(s)):
        if stack:
            if right_dict.get(s[i]) == stack[-1][0]:
                if s[i] == ")" and stack[-1][1] == i - 1:
                    if answer[-1] == "(":
                        answer.pop()
                    answer.extend(["2", "+"])
                if s[i] == ")" and stack[-1][1] != i - 1:
                    node = answer[-1]
                    if node == "+":
                        answer.pop()
                    answer.extend([")", "*2"])
                if s[i] == "]" and stack[-1][1] == i - 1:
                    if answer[-1] == "(":
                        answer.pop()
                    answer.extend(["3", "+"])
                if s[i] == "]" and stack[-1][1] != i - 1:
                    node = answer[-1]
                    if node == "+":
                        answer.pop()
                    answer.extend([")", "*3"])
                stack.pop()
            else:
                if answer[-1] == "*2" or answer[-1] == "*3":
                    answer.append("+")
                answer.append("(")
                stack.append([s[i], i])
        else:
            if i != 0:
                answer.append("+")
            answer.append("(")
            stack.append([s[i], i])
        # print(stack)
        # print(answer)

    if stack:
        return 0
    if answer[-1] == "+":
        answer = answer[:-1]
    answer = "".join(answer)
    # print(answer)

    answer = eval(answer)
    return answer


s = input()
# # ((2+3)*2+3)*2
# s = "(()[[]])([])"
# # s = "((()[])[])"
# # s = "()[()]"
# s = "((()[()]()[()])()(()[()]()[()])[])((()[()]()[()])()(()[()]()[()])[])"
# # ((2+(2*3)+2+(3*2))*2+2+(2+(3*2)+2+(3*2))*2*2+3)*2
# # s = "[()[()[()]]]"
# # s = "(()[()]()[()])(()[()]()[()])"
# # s = "[](()[()]()[()])(()[()]()[()])"
# # s = "[](()[()]()[()])()(()[()]()[()])"
# # s = "[](()[()]()[()])()(()[()]()[()])[]"
print(sol(s))


# https://www.acmicpc.net/board/view/62519
