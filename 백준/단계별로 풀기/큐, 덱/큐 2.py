import queue

my_queue = queue.Queue()
num = int(input())
for _ in range(num):
  command = input().split()
count = 0 
for count in range(len(command)):
  if command[i] == 'push':
      my_queue.put(command[i+1])
      count += 2
   elif command[i] == 'pop':
       if my_queue.qsize() != 0:
           my_queue.get()
       else:
           print(-1)
    elif command[i] == 'size':
        my_queue.qsize()
    elif command[i] == 'empty':
        if my_queue.qsize() == 0:
            print(1)
        else:
            print(0)
    elif command[i] == 'front':
        if my_queue.size() == 0:
            print(-1)
        my_queue.get()
    elif commandi] == 'back':
        if my_queue.size() == 0:
            print(-1)
