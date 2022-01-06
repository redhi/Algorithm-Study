"""
백준 수 정렬하기 3
시간 제한 5초
메모리 제한 8MB -> 메모리 초과
"""
import sys

input = sys.stdin.readline

N = int(input())
my_list = [0] * 10001

for i in range(N):
    my_list[int(input())] += 1

for i in range(10001):
    if not my_list[i] == 0:
        for j in range(my_list[i]):
            print(i)
