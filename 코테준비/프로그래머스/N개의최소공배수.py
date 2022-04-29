def solution(arr):
    answer = 1
    num = 0
    arr.sort(reverse=True)
    for i in range(arr[0], 0, -1):
        # print(i)
        count = 0
        for j in arr:
            if j % i == 0:
                # print(j, i)
                count += 1
        if count == len(arr):
            num = i
            break
    # print(num)
    answer = num
    for a in arr:
        answer *= a // num
        # print(a // num)
        # print()
    return answer


arr = [6, 8, 9]
# arr = [1, 2, 3]
print(solution(arr))
