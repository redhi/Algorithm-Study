from sys import stdin

num = stdin.readline() # 여러 줄의 입력을 받아야 할 떄 input보다 stdin이 더 효율적
my_deque = list()

for _ in range(int(num)):
    N,M = map(int,stdin.readline().split())
    my_list = list(map(int, stdin.readline().split()))
    goal = list(range(len(my_list))) # 해당 인덱스를 관리하기 위해 리스트 생성
    
    goal[M] = 'goal'
    print(goal)

    idx = 0
    for i in my_list:
        if i == max(my_list):
            idx += 1
            if goal[0] == 'goal':
                print(idx)
                break
            else:
                my_list.pop(0)
                goal.pop(0)
                print(my_list)
                print(goal)
        else:
            my_list.append(my_list.pop(0))
            goal.append(goal.pop(0))
