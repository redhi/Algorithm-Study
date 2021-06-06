N,M = map(int, input().split())
my_list = list(map(int ,input().split()))
my_queue = [i for i in range(1, N + 1)]

cnt = 0    
for i in range(M):
    queue_len = len(my_queue)
    queue_index = my_queue.index(my_list[i])
    
    if queue_index < queue_len - queue_index:
        while True:
            if my_queue[0] == my_list[i]:
                del my_queue[0]
                break
            else:
                my_queue.append(my_queue[0])
                del my_queue[0]
                cnt += 1
    else:
        while True:
            if my_queue[0] == my_list[i]:
                del my_queue[0]
                break
            else:
                my_queue.insert(0, my_queue[-1])
                del my_queue[-1]
                cnt += 1
print(cnt)
