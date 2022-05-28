from collections import Counter

T = int(input())
for i in range(T):
    num = int(input())
    arr = list(map(int, input().split()))
    print("#" + str(num), Counter(arr).most_common()[0][0])
