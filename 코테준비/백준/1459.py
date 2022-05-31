# 걷기
import sys

input = sys.stdin.readline
x, y, w, s = map(int, input().split())

minn = min(x, y)
maxx = max(x, y)
left = maxx - minn
answer = 0

answer1 = ((minn) * (w * 2)) + left * w
answer2 = s * minn + left * w

answer3 = 0
if (x + y) % 2 == 0:
    answer3 = maxx * s
else:
    answer3 = (maxx - 1) * s + w

answer = min(min(answer1, answer2), answer3)

print(answer)
