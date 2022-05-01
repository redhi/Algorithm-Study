def solution(s):
    answer = 1
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            nw = s[i:j]
            if nw == nw[::-1]:
                answer = max(len(nw), answer)

    return answer


s = "abcdcba"
s = "abacde"
print(solution(s))
