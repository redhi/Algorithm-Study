import sys

input = sys.stdin.readline

s = input().rstrip()
s_one = s.split("1")
s_zero = s.split("0")
one_num = len(s_one) - s_one.count("")
zero_num = len(s_zero) - s_zero.count("")

print(min(one_num, zero_num))
