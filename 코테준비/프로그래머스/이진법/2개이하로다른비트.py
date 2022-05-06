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
        answer.append(int(num))

    return answer


numbers = [2, 7]


print(solution(numbers))
