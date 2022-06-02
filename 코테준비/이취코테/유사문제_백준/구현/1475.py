# 방 번호
import sys

input = sys.stdin.readline
n = list(map(int, input().rstrip()))

d = {}
for i in range(0, 10):
    d[i] = 1

answer = 1
for num in n:
    if num == 6 or num == 9:
        if d.get(6) > 0:
            d[6] = d.get(6) - 1
        elif d.get(9) > 0:
            d[9] = d.get(9) - 1
        else:
            answer += 1
            for i in range(0, 10):
                if i != num:
                    d[i] = d.get(i) + 1
            d[num] = 0
    else:
        if d.get(num) > 0:
            d[num] = d.get(num) - 1
        else:
            answer += 1
            for i in range(0, 10):
                if i != num:
                    d[i] = d.get(i) + 1
            d[num] = 0
    # print(d, answer)

print(answer)
