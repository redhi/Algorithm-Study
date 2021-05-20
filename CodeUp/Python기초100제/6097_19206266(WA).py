h, w = map(int, input().split()) 
mylist = [[0]*w for i in range(h)]
num = int(input())
for i in range(num):
  l, d, x, y = map(int, input().split()) 
  for i in range(0,1):
    if d == 0: #가로일 경우
      mylist[x-1][y+i-1] = 1 # 행부분 1로 변경
    else:
      mylist[x+i-1][y-1] = 1 # 열부분 1로 변경
for i in mylist:
  print (" ".join(repr(j) for j in i))

