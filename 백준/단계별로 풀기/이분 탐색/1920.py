"""
백준 1920번 수 찾기
이분탐색을 이용하지 않고 set을 사용해 시간을 줄임
"""
import sys

input = sys.stdin.readline
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
