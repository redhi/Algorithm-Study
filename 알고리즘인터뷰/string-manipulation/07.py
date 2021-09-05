'''
07 두 수의 합
leetcode 1. Two Sum
'''
nums = input()
target = int(input())


def twosum(nums, target):
    #numdict = {}
    # for i in range(len(nums)):
    #    numdict[nums[i]] = i
    # print(numdict)
    #n_nums = [n for n in nums if n < target]
    # n_nums.sort(reverse=True)
    # print(n_nums)
    #count = 0
    #sub = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(i, j)
            if nums[i]+nums[j] == target:
                result = [i, j]
    print(result)


twosum([3, 3], 6)
