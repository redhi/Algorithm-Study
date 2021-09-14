'''
22. 일일 온도
'''


def Temp(T):

    stack = []
    answer = [0]*len(T)
    print(answer)

    for i, daily in enumerate(T):
        while stack and daily > T[stack[-1]]:
            print(T[stack[-1]])
            last = stack.pop()
            answer[last] = i-last
            print("현재", answer[last], i-last)
        stack.append(i)
        print(stack)

    return answer


Temp([73, 74, 75, 71, 69, 72, 76, 73])
T = [73, 74, 75, 69, 72, 76, 73]
