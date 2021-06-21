N = int(input())
my_list = list(map(int, input().split()))
my_stack = []
result = [-1 for _ in range(N)]

for i in range(len(my_list)):
    try:
        while my_list[my_stack[-1]] < my_list[i]:
            result[my_stack.pop()] = my_list[i]
    except:
        pass
        
    my_stack.append(i)
        
for i in range(N):
    print(result[i], end = ' ')
