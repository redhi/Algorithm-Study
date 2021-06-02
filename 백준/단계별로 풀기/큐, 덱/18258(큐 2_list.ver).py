from sys import stdin


num = stdin.readline() # input 대신 stdin.readlin() 사용
my_queue = []


count = 0 # deque를 이용하지 않고 리스트와 인덱스를 이용함
for _ in range(int(num)):
    command = list(stdin.readline().split()) # 한줄 씩 읽어서 사용
    if command[0] == 'push':
        my_queue.append(int(command[1]))
    elif command[0] == 'pop':
        if len(my_queue) > count:
            print(my_queue[count])
            count += 1            
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(my_queue)-count)
    elif command[0] == 'empty':
        if len(my_queue) == count: # 빈 리스트면 인덱스 초기화
            print(1)
            count = 0
        else:
            print(0)
    elif command[0] == 'front':
        if len(my_queue) > count:
            print(my_queue[count])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(my_queue) > count:
            print(my_queue[-1])
        else:
            print(-1)
