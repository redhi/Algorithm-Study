def solution(number, k):
    stack = []
    number = list(number)

    for i in range(len(number)):
        while k > 0 and stack and stack[-1] < number[i]:
            k -= 1
            stack.pop()

        stack.append(number[i])

    answer = "".join(stack[: len(stack) - k])
    return answer


number = "4177252841"
k = 4
print(solution(number, k))
