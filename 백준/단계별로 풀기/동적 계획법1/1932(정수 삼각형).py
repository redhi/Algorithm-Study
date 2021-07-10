N=int(input())
mylist=[]

for i in range(N):
  mylist.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(len(mylist[i])):
      if j == len(mylist[i])-1:
          mylist[i][j] = mylist[i][j] + mylist[i-1][j-1]
      elif j==0:
          mylist[i][j] = mylist[i][j] + mylist[i-1][j]
      else:
          mylist[i][j] = max(mylist[i-1][j-1] , mylist[i-1][j]) + mylist[i][j]
          
print(max(mylist[N-1]))
