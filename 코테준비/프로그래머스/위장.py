from collections import defaultdict


def solution(clothes):
    answer = 0
    dic = defaultdict(int)

    for i in range(len(clothes)):
        dic[clothes[i][1]] += 1
    l = list(dic.keys())

    for i in range(len(l)):
        dic[l[i]] += 1

    v = list(dic.values())
    t = 1

    for i in range(len(v)):
        t *= v[i]
    answer += t - 1

    return answer


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
print(solution(clothes))
