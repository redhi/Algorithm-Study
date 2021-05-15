n = int(input())

for i in range(1,n+1):
    if(i%3==0):
        continue
    print(i,end=" ") # end=" " 줄 바꿈하지 않고 출력
    
