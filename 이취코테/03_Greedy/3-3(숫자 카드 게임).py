N, M = map(int,input().split(" "))
arr = [[0]*M for i in range(N)] # N행 M열의 2차원 배열 선언
col_min = [] # 행의 최소값을 넣을 배열

for i in range(N):
        arr[i] = list(map(int, input().split(" "))) # 배열 대입
        
for j in range(N):
        col_min.append(min(arr[j])) # 각 행에서의 최소값을 대입
        
print(max(col_min)) # 그 중 가장 큰 값을 출력
