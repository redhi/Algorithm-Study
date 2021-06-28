N = int(input())
memo = {}

def fibo(num): # 메모이제이션 - 중복 계산을 줄여줌
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num in memo:
        return memo[num]

    memo[num] = fibo(num-1)+fibo(num-2) # 키값(num)에 해당하는 피보나치 계산 결과 넣어줌

    return memo[num]

print(fibo(N))
