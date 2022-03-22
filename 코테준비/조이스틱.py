"""
프로그래머스 조이스틱
"""

from collections import deque


def solution(name):
    answer = 0

    word = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    n = list(name)

    left, right = 0, 0
    for i in range(1, len(n)):
        if n[i] == "A" and (left + 1) == i:
            left += 1

    for i in range(len(n) - 1, 0, -1):
        if n[i] == "A" and (len(n) - 1 - right) == i:
            right += 1

    # print(left, right)

    for i in n:
        idx = word.index(i)

        if idx > 13:
            idx = 26 - idx
        answer += idx
        # print(idx)
    if left == 0 and right == 0:
        answer += len(n) - 1
    elif left == len(n) - 1:
        pass
    elif left >= right:
        answer += len(n) - 1 - left
    else:
        answer += len(n) - 1 - right

    # answer += len(n) - 1 - a_count

    print(answer)

    return answer


# JAAAJANAA
# 8 3
# J+1+1+1+N+1+1+J
# 1
# 1
# AAJJAJAA
# 1 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1
# aaaaaaaa
# jaaanani
# J + I
# aaaaajn
# 1 + n + 1 + j
# jaaaajna
# a<-j->a

# ajan
# 1+N+1+j
# ejan
# e+1+j+1+N
# ejana
# e+1+J+1+N
# eaajn
# e+1+N+1+J
# ejain
# e+1+j+1+I+1+N
# eaaan
# e+1+N

# len(word)-1-a의 갯수?

# 왼 오

# 0 1 2 3 4 5 6
# 1 2 3 6
# 0 4 5
# J+1+1+N+1+J
name = "ABAAAAABB"
solution(name)
# 3 7 -1 -4
# 4
# JAAJNAAA
# J+1+1+1+J+1+N

# a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

# z y x w v u t s r q  p  o  n
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# j e r o  e n
# 9 4 9 12 4 13
#  1 1 1 1 1
