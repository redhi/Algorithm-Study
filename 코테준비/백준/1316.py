import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
count = 0
for i in range(n):
    dic = defaultdict(list)
    s = input().rstrip()

    is_wrong = False
    for j in range(len(s)):
        if dic.get(s[j]):
            idx = dic.get(s[j])[-1]
            if idx + 1 != j:
                is_wrong = True
                break
            dic[s[j]].append(j)
        else:
            dic[s[j]].append(j)
    if not is_wrong:
        count += 1
print(count)
