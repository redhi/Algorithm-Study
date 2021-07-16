N = int(input())
arr = [[0]*N for i in range(N)] # N*N 행렬 초기화

command = list(input().split(" "))
#arr[0][0] = now # 현재 위치를 now로 표시
x = 0
y = 0
for i in command:
    if i == "L":
        if 0 < y <= N-1:
            y -= 1
        else:
            pass
    if i == "R":
        if 0 <= y <= N-1:
            y += 1
        else:
            pass
    if i == "U":
        if 0 < x <= N-1:
            x -= 1
        else:
            pass
    if i == "D":
        if 0 <= x <= N-1:
            x += 1
        else:
            pass
x += 1
y += 1
print(x,y)
