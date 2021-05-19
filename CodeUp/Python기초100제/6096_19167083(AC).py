mylist = [[]*19 for _ in range(19)] # 2차원 배열선언
for i in range(19):
   mylist[i]=list(map(int,input().split()))

num = int(input())

for i in range(num):
    x,y=map(int,input().split())
    
    for j in range(19):
        if(mylist[x-1][j]==1):
            mylist[x-1][j]=0
        else:
            mylist[x-1][j]=1
    for j in range(19):
        if(mylist[j][y-1]==1):
            mylist[j][y-1]=0
        else:
            mylist[j][y-1]=1

for i in range(19):
    for j in range(19):
        print(mylist[i][j],end=' ')
    print()

