from itertools import combinations


def solution(nums):
    answer = 0
    l = list(map(list, combinations(nums, 3)))
    for i in l:
        num = sum(i)
        is_prime = True
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
