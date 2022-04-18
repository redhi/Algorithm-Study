def solution(n, times):
    answer = 0
    n = n - len(times)
    times.sort()

    # 7 14 21 2
    # 10 20
    return answer


n = 6

times = [7, 10]
print(solution(n, times))
