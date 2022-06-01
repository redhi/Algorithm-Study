import sys

input = sys.stdin.readline
n = input().rstrip()

a, b = n[: len(n) // 2], n[len(n) // 2 :]
a = list(map(int, a))
b = list(map(int, b))

answer = "READY"
if sum(a) == sum(b):
    answer = "LUCKY"

print(answer)
