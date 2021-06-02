from collections import deque # from collections import deque 의 형태로 써야 함 (컨테이너 데이터형)

my_deque = deque() # 덱 선언 방식

num = int(input())

for i in range(num):
    my_deque.append(i+1)
    
count = 1
while(len(my_deque) != 1): # 덱이 하나남을 때까지 반복
    if(count%2==1):
        my_deque.popleft() # 맨 처음 데이터 꺼내기
    else:
        my_deque.rotate(-1) # 음수면 왼쪽으로 회전
    count += 1

print(my_deque.pop())
