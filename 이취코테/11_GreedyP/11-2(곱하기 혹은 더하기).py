num_arr = list(map(int, input()))
memo = 0 # 그전 값을 저장하기 위한 변수
result = 0

for num in num_arr: # num은 현재 값
    if memo == 0 and result != 0: # 그전 값이 0이고 결과값이 0이 아닐 때
        # 20984같은 경우
        result *= num
        memo = num
    elif result == 0 or num == 0: # 처음 0일 경우와 다음에서 0이 나올 경우
        # 02984같은 경우
        result += num
        memo = num
    else:
        result *= num
        memo = num

print(result)
        
        
