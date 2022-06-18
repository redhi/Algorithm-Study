import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for mm in m_list:
    start = 0
    end = len(n_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == mm:
            print("yes", end=" ")
            break
        elif n_list[mid] > mm:
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        print("no", end=" ")
