T = int(input())
for i in range(T):
    item = input()
    my_list = list(item)
    print(my_list)
    sum = 0
    for i in my_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
