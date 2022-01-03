"""
백준 크로아티아 알파벳
구현 문자열
"""
from collections import deque

cro_dict = dict()
cro_dict = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = list(input())
d = deque()
count = 0
for i in range(len(word)):
    d_word = "".join(d) + word[i]

    in_for = False
    for j in range(len(cro_dict)):
        if cro_dict[j] in d_word:
            d_word = "".join(d) + word[i]
            in_for = True
            num = len(d_word) - len(cro_dict[j]) + 1
            d.clear()

            count += num
    if in_for == False:
        d.append(word[i])
print(count + len(d))
