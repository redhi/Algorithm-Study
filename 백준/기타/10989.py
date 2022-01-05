"""
백준 수 정렬하기 3
시간 제한 5초
메모리 제한 8MB -> 메모리 초과
"""
import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    heapq.heappush(heap, int(input()))

while not len(heap) == 0:
    print(heapq.heappop(heap))
