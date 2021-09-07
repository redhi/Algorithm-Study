'''
09 세 수의 합
leetcode 15. 3Sum

타임아웃
'''
nums = input()


class twos(object):
    def __init__(self, tsum):
        self.tsum = tsum

    def __int__(self):
        return self.tsum

    def __repr__(self):
        return repr(self.tsum)


def sums(nums):
    sumdict = {}
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            # print(len(nums)-1)
            print(i, j)
            new_n = nums[:]  # 인덱스
            del new_n[i]
            new_n.remove(nums[j])
            print(new_n)
            sumdict[twos(nums[i]+nums[j])] = [nums[i], nums[j], new_n]
    print(sumdict)
    result = []
    for two, rest in sumdict.items():
        for i in rest[2]:

            if (0-int(two)) == i:
                result.append([rest[0], rest[1], i])
    # 2차원 배열 중복 제거
    print(result)
    nn_result = []
    for item in result:
        print("전", item)
        item = sorted(item)
        print("후", item)
        nn_result.append(item)
    result = nn_result
    print(result)

    result = list(set([tuple(set(item)) for item in result]))
    print(result)
    n_result = []
    for item in result:
        item = list(item)
        # print(item)
        if len(item) == 2:
            print(list(item))
            item.append(0-sum(item))
            n_result.append(item)
        elif len(item) == 1:
            item.append(0)
            item.append(0)
            n_result.append(item)
        else:
            n_result.append(item)
    print(n_result)


sums([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
