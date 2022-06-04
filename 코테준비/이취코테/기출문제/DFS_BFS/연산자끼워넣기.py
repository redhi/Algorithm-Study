import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))

total = []
for i in range(4):
    for j in range(oper[i]):
        total.append(i)

oper_list = list(map(list, permutations(total, n - 1)))

new = arr[1:]
num_list = set()
for ope in oper_list:
    num = arr[0]
    for nn, o in zip(new, ope):
        if o == 0:
            num = num + nn
        elif o == 1:
            num = num - nn
        elif o == 2:
            num = num * nn
        else:
            if num < 0:
                num = abs(num)
                num = num // nn
                num = -num
            else:
                num = num // nn
    num_list.add(num)

print(max(num_list))
print(min(num_list))
