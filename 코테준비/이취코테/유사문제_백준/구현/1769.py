# 3의 배수
import sys

input = sys.stdin.readline
x = list(map(int, list(input().rstrip())))

count = 0
while len(x) > 1:
    x = sum(x)
    x = list(map(int, list(str(x))))
    count += 1

sum_x = x[0]
print(count)
if sum_x % 3 == 0:
    print("YES")
else:
    print("NO")
