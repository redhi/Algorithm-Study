from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    arr = set()
    for i in range(len(numbers)):
        pre_arr = list(map(list, permutations(numbers, i + 1)))
        for j in range(len(pre_arr)):
            # print("".join(map(str, pre_arr[j])))
            arr.add(int("".join(map(str, pre_arr[j]))))
        # arr.extend(list(map(list, permutations(numbers, i + 1))))
    arr = list(arr)
    for i in range(len(arr)):
        if arr[i] == 0 or arr[i] == 1:
            continue
        num = arr[i]
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    # print(arr)
    return answer


numbers = "011"
print(solution(numbers))
