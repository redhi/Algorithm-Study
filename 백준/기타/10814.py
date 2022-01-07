"""
백준 나이순 정렬
정렬
"""
import sys

input = sys.stdin.readline

N = int(input())
age_list = []

for i in range(N):
    age, name = input().split()
    age_list.append([int(age), name, i])
age_list.sort(key=lambda x: (x[0], x[2]))

for i in range(N):
    print(age_list[i][0], age_list[i][1])
