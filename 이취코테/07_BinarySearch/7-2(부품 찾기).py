N = int(input())
num_arr = list(map(int, input().split()))

M = int(input())
num_arr2 = list(map(int, input().split()))

for i in num_arr2:
    if i in num_arr:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
