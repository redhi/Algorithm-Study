import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
# print(arr)
# s_arr = "".join(map(str, arr))
def is_r(s, e):
    m = (s + e) // 2
    while s != m and e != m:
        if arr[s] == arr[e]:
            # print("히히", arr[s - 1], arr[e - 1])
            s += 1
            e -= 1
        else:
            # print("엥", arr[s - 1], arr[e - 1])
            return False

    return True


an = []
for i in range(n):
    for j in range(i, n, 2):
        if is_r(i, j):
            an.append([i + 1, j + 1])
        # print(i, j)
# print(an)
for i in range(m):
    s, e = map(int, input().split())
    if s == e:
        print(1)
    elif an.count([s, e]) == 1:
        print(1)
    else:
        print(0)

    # print(s,e)
