mylist = [list(map(int, input().split())) for _ in range(10)]
num = 1
j2 = 1   
for i in range(1,10):
    if(num==2):
        break
    for j in range(1,10):
        if(mylist[i][j2]==0):
            mylist[i][j2]=9
            j2 += 1
            continue
        elif(mylist[i][j2]==1):
            j2 -= 1
            break
        elif(mylist[i][j2]==2):
            mylist[i][j2]=9
            num = 2
            break
for i in range(10):
    for j in range(10):
        print(mylist[i][j],end=' ')
    print()
