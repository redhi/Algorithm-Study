"""
프로그래머스
"""
import math


def solution(str1, str2):
    answer = 0
    lowstr1 = str1.lower()
    lowstr2 = str2.lower()

    list_str1 = [
        lowstr1[i : i + 2]
        for i in range(0, len(lowstr1) - 1)
        if lowstr1[i : i + 2].isalpha()
    ]
    list_str2 = [
        lowstr2[i : i + 2]
        for i in range(0, len(lowstr2) - 1)
        if lowstr2[i : i + 2].isalpha()
    ]
    set1 = [[i] for i in list_str1]
    set2 = [[i] for i in list_str2]
    alen = len(set1) + len(set2)

    for i in range(len(list_str1)):
        set1[i].append(list_str1.count(list_str1[i]))
    set1 = set(list(map(tuple, set1)))

    for i in range(len(list_str2)):
        set2[i].append(list_str2.count(list_str2[i]))
    set2 = set(list(map(tuple, set2)))
    # print(set1)
    # print(set2)

    count = 0

    for i in set1:
        s1 = i[0]
        n1 = i[1]
        for j in set2:
            s2 = j[0]
            n2 = j[1]
            if s1 == s2:
                n1 = min(n1, n2)
                count += n1
    rall = alen - count
    if rall == 0:
        answer = 65536
        return answer
    answer = math.trunc((count / rall) * 65536)
    # print(answer)

    return answer


str1 = "E=M*C^2"
str2 = "e=m*c^2"
str3 = "shake hands"
solution(str1, str2)
