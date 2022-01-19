"""
백준 셀프 넘버
"""

n_num = set(range(1, 10001))
new_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new_num.add(i)

s_num = sorted(n_num - new_num)
for i in s_num:
    print(i)
