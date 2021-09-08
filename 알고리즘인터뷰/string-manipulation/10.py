'''
10 배열 파티션 1
leetcode Array Parition 1
'''
s = input()


def parition(s):
    s.sort(reverse=True)
    sum = 0
    pair = []

    for i in s:
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair[]

    print(sum)


parition([1, 4, 3, 2, 7, 10])
