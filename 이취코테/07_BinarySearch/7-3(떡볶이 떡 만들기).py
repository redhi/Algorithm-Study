N, M = map(int,input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
left = []
cut = arr[0]

while cut>0:
    for i in range(N):
        if arr[i] < cut:
            left.append(0)
        else:
            left.append(arr[i]-cut)
    print(cut, left)
    if sum(left)== M:
        break
    cut -= 1
    left.clear()

print(cut)
