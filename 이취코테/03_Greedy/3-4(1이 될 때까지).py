N, K = map(int, input().split(" "))
count = 0
while(True):
    if N%K == 0: # N이 K로 나누어 떨어지면
        N = N/K # N에 N/K의 값을 넣는다
        count += 1
    else:
        N -= 1 # N에 N-1값을 넣는다
        count += 1

    if N == 1: # N이 1이 되면
        break # while문 탈출

print(count)
