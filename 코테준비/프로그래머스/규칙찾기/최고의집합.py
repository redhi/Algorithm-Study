def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    init = s // n
    for i in range(n):
        answer.append(init)
    left = s % n
    for i in range(left):
        answer[i] += 1
    answer.sort()
    return answer


n = 2
s = 9
print(solution(n, s))
