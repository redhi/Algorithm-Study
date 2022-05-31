# 수들의 합2
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
left, right = 0, 1
while left <= right and right <= n:
    total = sum(arr[left:right])

    if total == m:
        count += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(count)

# 1234
# 234
# 34
