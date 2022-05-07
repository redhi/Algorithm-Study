from collections import defaultdict


def solution(nums):
    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1
    n = len(nums) // 2
    dic_num = len(dic)
    if dic_num < n:
        return dic_num

    return n


nums = [3, 1, 2, 3]

print(solution(nums))
