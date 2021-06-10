K = int(input())
my_list = []
for i in range(K):
    num = int(input())
    if num == 0:
        my_list.pop()
    else:
        my_list.append(num)
print(sum(my_list))
