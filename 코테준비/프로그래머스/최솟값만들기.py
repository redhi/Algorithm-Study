def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i, j in zip(A, B):
        answer += i * j

    return answer


A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
