# 리모컨
import sys

input = sys.stdin.readline

channel = map(int, input())
m = map(int, input())
broken = list(map(int, input().split()))
now = 100
min_count = abs(100-channel)
for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_count = min(abs(int(nums) - channel) + len(nums), min_count)


print(min_count)
# 5455++
# 5459--
# 77777
