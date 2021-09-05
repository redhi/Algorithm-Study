'''11 자신을 제회한 배열의 곱
leetcode 238. Product of Array Except Self
'''
import collections

s = input()


def product(nums):
    new_s = nums[:]
    nums = collections.deque(nums)
    new_s = collections.deque(new_s)

    result = []
    for i in range(len(nums)):
        new_s.rotate(-(1))
        new = list(new_s)[:-1]

        pro = 1
        for n in new:
            pro *= n
        result.append(pro)
    return result


print(product([1, 2, 3, 4]))
