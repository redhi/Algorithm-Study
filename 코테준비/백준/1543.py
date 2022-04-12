import sys

input = sys.stdin.readline

s = input().rstrip()
b = input().rstrip()

s = s.replace(b, "*")
print(s.count("*"))
