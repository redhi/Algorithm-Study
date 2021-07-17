num_arr = list(map(int, input()))
result = 0

num_arr.sort() # 정렬
zero = num_arr.count(0) # 0의 개수를 센다
new_arr = num_arr[zero:] # 0을 제외한 리스트를 새로 선언


for num in new_arr:
    if new_arr[0] == num:
        result = num
    else:
        result *= num


print(result)
