def solution(stones, k):
    answer = 0
    # 이분탐색 : 중간값찾기
    left = 0
    right = max(stones)

    while left <= right:
        count = 0
        mid = (left + right) // 2
        for s in stones:
            if s - mid <= 0:
                count += 1
            else:
                count = 0  # 연속되지 않은 경우니까
            if count >= k:
                break
        if count >= k:
            answer = mid  # 정답갱신
            right = mid - 1  # 이진탐색의 범위를 내림
        else:
            left = mid + 1  # 이진탐색의 범위를 올림

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# stones = [3, 3, 4, 4, 3, 4, 3, 3, 1, 3]
k = 3

print(solution(stones, k))
