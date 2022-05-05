def numTimesAllBlue(flips):
    mx = res = 0
    for i in range(len(flips)):
        mx = max(mx, flips[i])
        res += mx == i + 1
        # print(res, mx, i)
    return res


# 00000
# 00001
# 10001
# 00100

flips = [5, 1, 2, 3, 4]
flips = [3, 5, 1, 4, 5]
print(numTimesAllBlue(flips))
