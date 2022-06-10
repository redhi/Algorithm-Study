# 단어의 개수
import sys

input = sys.stdin.readline

s = input().strip().split(" ")
count = 0

for ss in s:
    if ss != "":
        count += 1
print(count)
