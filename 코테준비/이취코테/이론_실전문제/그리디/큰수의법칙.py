import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
new = [arr[0] for _ in range(k)] + [arr[1]]

left = m % (k + 1)

new2 = []
if left == 1:
    new2 = [new[0]]
else:
    new2 = new[:left]
answer = sum(new) * (m // (k + 1)) + sum(new2)

print(answer)
