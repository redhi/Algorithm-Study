# 3의 배수
import sys

input = sys.stdin.readline
x = int(input())

x = list(map(int, list(str(x))))
count = 0
while len(x) > 1:
    x = sum(x)
    x = list(map(int, list(str(x))))
    # print(x)
    count += 1
sum_x = sum(x)
print(count)
if sum_x % 3 == 0:
    print("YES")
else:
    print("NO")
