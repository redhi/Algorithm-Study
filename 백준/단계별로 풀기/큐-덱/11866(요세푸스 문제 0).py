from collections import deque

N, K = map(int, input().split())

my_deque = deque()
newlist = list() # 요세푸스 순열을 넣어줄 리스트 선언

for i in range(1,N+1):
    my_deque.append(i)

rotNum = K-1 # 회전을 하여 값을 꺼내기위해 변수 선언 
while len(my_deque) != 0:
    my_deque.rotate(-rotNum)
    newlist.append(my_deque.popleft())

print('<',end='')
for i in range(len(newlist)):
    if i == len(newlist)-1: # 마지막 값은 , 생략
        print(newlist[i], end='')
    else:
        print(newlist[i],end=', ')
print('>',end='')
