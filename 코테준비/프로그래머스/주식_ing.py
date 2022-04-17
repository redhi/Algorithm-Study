def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    time = -1
    for i in range(len(prices)):
        time += 1
        if stack:
            while stack[-1] > prices[i]:
                d = stack.pop()
                answer[i - 1] = d
                print(d, i)
            stack.append(prices[i])

            pass
        else:
            stack.append(prices[i])
        print(stack, time, i)
    return answer


prices = [1, 2, 3, 2, 3]

print(solution(prices))
