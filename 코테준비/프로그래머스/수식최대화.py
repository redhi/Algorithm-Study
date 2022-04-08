from itertools import permutations


def solution(expression):
    answer = 0
    oper = ["*", "+", "-"]
    oper_list = list(map(list, permutations(oper, 3)))
    exp_list = []

    idx = 0
    for i in range(len(expression)):
        if expression[i] == "*" or expression[i] == "-" or expression[i] == "+":
            exp_list.append(expression[idx:i])
            exp_list.append(expression[i])
            idx = i + 1
    exp_list.append(expression[idx:])

    for oper in oper_list:
        stack = [[] for _ in range(3)]
        for ope in range(len(oper)):
            o = oper[ope]
            if not stack[0]:
                compare_list = exp_list
            else:
                compare_list = stack[ope - 1]
            idxx = len(compare_list)
            for i in range(len(compare_list)):
                if i >= idxx:
                    idxx = len(compare_list)
                    continue
                if stack[ope]:
                    if compare_list[i] == o:
                        left = stack[ope].pop()
                        right = compare_list[i + 1]
                        stack[ope].append(eval(str(left) + o + str(right)))
                        idxx = i + 1
                    else:
                        stack[ope].append(compare_list[i])
                else:
                    stack[ope].append(compare_list[i])

        answer = max(abs(stack[ope][0]), answer)

    return answer


expression = "100-200*300-500+20"

print(solution(expression))
