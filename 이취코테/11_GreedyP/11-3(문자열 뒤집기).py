mystr = list(map(int, input()))
count1 = 0
count0 = 0

# 시작할 때마다 연속된 0,1 숫자열을 센다
if mystr[0] == 1: # 처음에 연속 문자열을 먼저 카운트
    count1 = 1
else:
    count0 = 1
    
for i in range(len(mystr)-1):
    if mystr[i] != mystr[i+1]:  # 현재 숫자와 다음 숫자가 다르면
        if mystr[i+1] == 1:  # 다음 숫자가 1이면
            count1 += 1  # 1로 연속이 바뀐 경우 카운트
            
        else:
            count0 += 1 # 0으로 연속이 바뀐 경우 카운트
        

print(min(count1, count0))
