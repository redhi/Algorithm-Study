def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    time = 0
    for i in range(len(prices)):
        time += 1
        if stack:
            while stack[-1][0] > prices[i]:
                d, s_time, idx = stack.pop()
                spent = time - s_time
                answer[idx] = spent

                if not stack:
                    break
                # print(d, i, spent)
            stack.append([prices[i], time, i])

        else:
            stack.append([prices[i], time, i])
        # print(stack, time, i)
    for i in range(len(stack)):
        idx = stack[i][2]
        answer[idx] = len(prices) - stack[i][1]
    return answer


prices = [3, 2, 1, 2, 3, 1]

print(solution(prices))
