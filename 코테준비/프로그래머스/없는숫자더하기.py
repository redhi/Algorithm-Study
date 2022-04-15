def solution(numbers):
    answer = 0
    dic = {}
    for i in range(len(numbers)):
        dic[numbers[i]] = 1
    for i in range(10):
        if not dic.get(i):
            answer += i
    return answer


numbers = [1, 2, 3, 4, 6, 7, 8, 0]

print(solution(numbers))
