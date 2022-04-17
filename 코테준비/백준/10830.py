import sys


def matrixM(arr, bb):
    bb = list(map(list, zip(*bb)))
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            now = 0
            for x, y in zip(arr[i], bb[j]):
                now += x * y
            temp[i][j] = now % 1000
    arr = temp
    return arr


input = sys.stdin.readline
n, b = map(int, input().split())
arr = [[] for _ in range(n)]
B = bin(b)[2:]

for i in range(n):
    arr[i].extend(map(int, input().split()))

identity_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
result = identity_matrix[:]

for i in range(len(B)):
    if B[-i - 1] == "1":
        temp1 = arr[:]
        while i != 0:
            temp1 = matrixM(temp1, temp1)
            i -= 1
        result = matrixM(result, temp1)

for row in result:
    print(*row)
