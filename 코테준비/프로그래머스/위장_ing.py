from collections import defaultdict


def solution(clothes):
    answer = 0
    dic = defaultdict(list)
    for i in range(len(clothes)):
        # if dic.get(clothes[i][1]):
        dic[clothes[i][1]].append(clothes[i][0])
    dic_len = len(dic.keys())
    l = list(dic.keys())
    # print(dic_len, dic.keys())
    answer += len(clothes)
    if dic_len > 1:
        num = 1
        for i in l:
            num *= len(dic[i])
        # print(num)
        answer += num
    # print(dic)
    return answer


clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
print(solution(clothes))
