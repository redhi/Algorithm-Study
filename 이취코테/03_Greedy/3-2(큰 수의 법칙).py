N, M, K = map(int,input().split(" "))
arr = []
arr = input().split(" ")

total = 0
repeat = M//K # 특정 인덱스 반복 덧셈 횟수
leftover = M%K # 나머지 덧셈 횟수
arr.sort() # 배열을 정렬

for i in range(repeat):
    total += int(arr[-1])*K # K번만큼 가장 큰 원소를 더함
   
for j in range(leftover):
    total += int(arr[-2]) # 그 다음으로 큰 원소를 더해준다.

print(total)