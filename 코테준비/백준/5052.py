import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    arrr = [[] for _ in range(n)]
    for j in range(n):
        tell = input().rstrip()
        arr.append(tell)
    arr.sort()
    is_break = False
    for j in range(n - 1):
        if arr[j] == arr[j + 1][: len(arr[j])]:
            # print("허", arr[k])
            is_break = True
            break
    if is_break:
        print("NO")
    else:
        print("YES")
