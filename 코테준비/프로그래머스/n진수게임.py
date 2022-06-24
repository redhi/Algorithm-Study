from collections import deque


def solution(n, t, m, p):
    answer = ""
    num_arr = fun(n, t * m)
    answer = []

    for i in range(p - 1, m * (t), m):
        answer.append(str(num_arr[i]))
    answer = "".join(answer)

    return answer


def fun(n, num):
    alpha_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    num_arr_list = []
    for i in range(num + 1):
        num_arr = deque()
        num1 = i
        num2 = 0
        if num1 == 0:
            num_arr.appendleft(0)
        while num1 != 0:
            num2 = num1 % n
            num1 //= n
            if alpha_dict.get(num2):
                num_arr.appendleft(alpha_dict.get(num2))
            else:
                num_arr.appendleft(num2)
        num_arr = list(num_arr)
        num_arr_list.extend(num_arr)
    return num_arr_list


n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))
