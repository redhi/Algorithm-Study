a,b,c = map(int,input().split())
count = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            print('{} {} {}'.format(i,j,k)) # print(i,j,k) 보다 실행시간 빠름
            count += 1
                
print(count)
