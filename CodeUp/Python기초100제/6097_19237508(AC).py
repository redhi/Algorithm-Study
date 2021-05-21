h, w = map(int, input().split()) 
mylist = [[0]*w for _ in range(h)]
num = int(input())
for i in range(num):
  l, d, x, y = map(int, input().split())
  
  for j in range(l):
      if d == 0:
          mylist[x-1][y+j-1] = 1 
      else:
          mylist[x+j-1][y-1] = 1 
          
for i in range(h):
    for j in range(w):
        print(mylist[i][j],end=' ')
    print()
  
