'''
10 배열 파티션 1
leetcode Array Parition 1
'''
s = input()


def parition(s):
    s.sort(reverse=True)
    sum = 0

    for i in range(len(s)//2):
        sum += s[(2*i)+1]
    print(sum)


parition([1, 4, 3, 2, 7, 10])
