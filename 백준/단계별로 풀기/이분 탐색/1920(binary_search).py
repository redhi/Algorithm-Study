"""
백준 1920번 수 찾기
이분탐색을 이용
"""
import sys

input = sys.stdin.readline
N = int(input())
a = sorted(list(map(int, input().split())))
M = int(input())
b = list(map(int, input().split()))

def bs(i, a, start, end):
    if start>end:
        return 0
    mid = (start+end)//2
    if a[mid] == i:
        return 1
    elif i < a[mid]:
        return bs(i, a, start, mid-1)
    else:
        return bs(i,a,mid+1,end)

for i in b:
    start = 0
    end = len(b) - 1
    print(bs(i, a, start, end))
