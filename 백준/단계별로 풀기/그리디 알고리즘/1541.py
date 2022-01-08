"""
백준 잃어버린 괄호
"""
import sys

input = sys.stdin.readline().rstrip
my_list = input().split("-")
num_list = []

for i in my_list:
    plus = list(map(int, i.split("+")))
    plus_num = sum(plus)
    num_list.append(plus_num)
result = num_list[0]
for i in range(1, len(num_list)):
    result -= num_list[i]
print(result)
