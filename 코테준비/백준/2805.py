# 나무 자르기
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort(reverse=True)

start = 1
end = tree[0]
mid = (start + end) // 2
answer = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for t in tree:
        if mid < t:
            total += t - mid

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)

# 6 4 10
