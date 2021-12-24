def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    # 원소의 범위는 가장 커도 1000이하이므로
    numbers=sorted(numbers, key=lambda x:x*3, reverse=True) # 스트링이라서 앞자리 수가 중요
    answer = "".join(numbers)
    return str(int("".join(numbers))) # int에서 str로 두번 형변환 [0,0,0,0]

arr=[6, 10, 2]
print(solution(arr))

arr2 =["222","9","30"]
print(solution(arr2))

arr3=[0,0,0,0]
print(solution(arr3)) # 여기서 0000이 나옴
