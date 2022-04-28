from collections import defaultdict


def solution(str1, str2):
    answer = 0
    set1,set2 = set(),set()
    dict1, dict2 = defaultdict(int), defaultdict(int)

    for i in range(len(str1)):
        s = str1[i : i + 2]
        if len(s) == 2 and s.isalpha():
            set1.add(s.lower())
            dict1[s.lower()] += 1

    for j in range(len(str2)):
        s = str2[j : j + 2]
        if len(s) == 2 and s.isalpha():
            set2.add(s.lower())
            dict2[s.lower()] += 1

    uni = list(set1 & set2)
    sum_set = list(set1 | set2)

    u_sum = 0
    for i in range(len(uni)):
        u_sum += min(dict1[uni[i]], dict2[uni[i]])
    s_sum = 0
    for i in range(len(sum_set)):
        s_sum += max(dict1[sum_set[i]], dict2[sum_set[i]])

    if s_sum == 0:
        answer = 65536
    else:
        answer = int((u_sum / s_sum) * 65536)
    return answer


str1 = "FRANCE"
str2 = "french"
# str1 = "handshake"
# str2 = "shake hands"
# str1 = "aa1+aa2"
# str2 = "AAAA12"
print(solution(str1, str2))
