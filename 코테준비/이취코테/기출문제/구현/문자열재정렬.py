import sys

input = sys.stdin.readline
s = list(input().strip())
s.sort()

num, idx = 0, 0

for i in range(len(s)):
    if not s[i].isdigit():
        idx = i
        break
    else:
        num += int(s[i])

print("".join(s[i:]) + str(num))
