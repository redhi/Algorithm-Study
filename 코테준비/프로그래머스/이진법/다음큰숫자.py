def solution(n):
    answer = n
    bin_n = bin(n)[2:].count("1")
    while True:
        answer += 1
        if bin(answer)[2:].count("1") == bin_n:
            break
    return answer


n = 78
print(solution(n))
