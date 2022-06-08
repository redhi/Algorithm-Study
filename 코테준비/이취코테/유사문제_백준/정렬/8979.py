import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
dic = defaultdict(int)
for _ in range(n):
    idx, gold, silver, copper = map(int, input().split())
    arr.append([idx, gold, silver, copper])
    dic[str([gold, silver, copper])] = 0

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if dic.get(str([arr[i][1], arr[i][2], arr[i][3]])) == 0:
        dic[str([arr[i][1], arr[i][2], arr[i][3]])] = i + 1

for i in range(n):
    if arr[i][0] == k:
        print(dic.get(str([arr[i][1], arr[i][2], arr[i][3]])))
        break
