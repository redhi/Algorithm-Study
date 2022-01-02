from sys import stdin

num = stdin.readline() # 여러 줄의 입력을 받아야 할 떄 input보다 stdin이 더 효율적

for _ in range(int(num)):
    N,M = map(int,stdin.readline().split())
    my_list = list(map(int, stdin.readline().split())) # 덱으로 선언하면 map 사용 불가
    goal = list(range(len(my_list))) # 해당 인덱스를 관리하기 위해 리스트 생성
    goal[M] = 'goal'
  
    idx = 0 # 나가는 순서
    while True:
        
        if my_list[0] == max(my_list):
            idx += 1 # 빠져나갈 때만 +1
            if goal[0] == 'goal':
                print(idx)
                break
            else:
                my_list.pop(0)
                goal.pop(0)
                
        else:
            my_list.append(my_list.pop(0)) # 해당 리스트내에 가장 큰 값아니면 뒤에 붙이기
            goal.append(goal.pop(0))
