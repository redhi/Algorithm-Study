import sys

input = sys.stdin.readline

s = input().rstrip()
dire = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

i = int(s[1]) - 1
j = ord(s[0]) - ord("a")

answer = 0
for d in dire:
    if 0 <= i + d[0] < 8 and 0 <= j + d[1] < 8:
        answer += 1

print(answer)
