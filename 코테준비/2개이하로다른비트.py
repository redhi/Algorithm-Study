def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            binary_num = list(bin(n)[2:])
            binary_num[-1] = "1"
        else:
            binary_num = bin(n)[2:]
            binary_num = "0" + binary_num
            zero_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[zero_idx] = "1"
            binary_num[zero_idx + 1] = "0"
        num = int("".join(binary_num), 2)
        answer.append(num)

    return answer


# def fun(num):
#     left_num = 0
#     num1 = num
#     bin_list = [0] * 25
#     bin = []
#     while num1 != 0:
#         left_num = num1 % 2
#         bin.append(left_num)
#         num1 //= 2
#     # bin.reverse()
#     for i in range(len(bin)):
#         bin_list[-(i + 1)] = bin[i]
#     # print(idx)
#     return bin_list


# def check(num):
#     bin_list = fun(num)
#     num1 = num + 1
#     is_right = True
#     while is_right:
#         bin_list2 = fun(num1)
#         count = 0
#         wrong = 0
#         for i in range(len(bin_list) - 1, 1, -1):
#             if bin_list[i] != bin_list2[i]:
#                 if count < 2:
#                     count += 1
#                 else:
#                     wrong = 1
#                     break
#         if wrong == 0:
#             is_right = False
#         else:
#             num1 += 1

#     # print("숫자야", num1)
#     return num1


numbers = [2, 7]


print(solution(numbers))
