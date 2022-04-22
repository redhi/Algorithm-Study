import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for i in range(n):
    times.append(int(input()))


def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    while left <= right:
        count = 0
        mid = (left + right) // 2
        for t in times:
            pre_count = mid // t
            if pre_count >= 0:
                count += pre_count
            if count >= n:
                break
        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution(m, times))
