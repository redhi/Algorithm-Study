import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nature_list = [int(input()) for _ in range(n)]

result_list = []
result_list.append(int(round(sum(nature_list) / len(nature_list), 0)))

nature_list.sort()
result_list.append(nature_list[len(nature_list) // 2])

most_list = Counter(nature_list).most_common(2)
if len(most_list) == 1:
    most_value = most_list[0][0]
else:
    if most_list[0][1] == most_list[1][1]:
        most_value = most_list[1][0]
    else:
        most_value = most_list[0][0]
result_list.append(most_value)

result_list.append(max(nature_list) - min(nature_list))

for i in range(len(result_list)):
    print(result_list[i])
