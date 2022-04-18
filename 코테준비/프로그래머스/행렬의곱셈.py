
def solution(arr1, arr2):
    temp = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                temp[i][j] += arr1[i][k] * arr2[k][j]

    return temp


# 2행0열
# 14 33 3
# 32 32 3
# 41     2
# 891
# 232 54
# 424 24
# 314 31
# arr1 = [[1, 4, 1], [3, 2, 1], [4, 1, 1], [8, 9, 1]]
arr1 = [[-1, 4], [3, 2], [4, 1]]
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[3, 3, 2], [1, 2, 3]]
arr2 = [[-3, 3], [3, 3]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1, arr2))
