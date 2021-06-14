while True:
    my_line = input()
    if my_line == '.':
        break
    my_list = []
    temp = True
    for i in my_line:
        if i == '(' or i == '[':
            my_list.append(i)
        elif i == ')':
            if not my_list or my_list[-1] == '[':
                temp = False
                break
            elif my_list[-1] == '(':
                my_list.pop()
        elif i == ']':
            if not my_list or my_list[-1] == '(':
                temp = False
                break
            elif my_list[-1] == '[':
                my_list.pop()
    if temp == True and not my_list:
        print('yes')
    else:
        print('no')
