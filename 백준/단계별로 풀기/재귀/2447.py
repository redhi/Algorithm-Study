'''
2447번 별찍기 - 10
'''

n = int(input())
arr = [["*"]*n for _ in range(n)]


def starwrite(N):
    if N == 3:
        arr[1][1] = " "
        for i in range(n):
            print("".join(arr[i]))
    else:
        for i in range(n):
            arr[4: -3] = " "
        for i in range(n):
            print("".join(arr[i]))


# for i in range(n):
    print("".join(arr[i]))


starwrite(n)
