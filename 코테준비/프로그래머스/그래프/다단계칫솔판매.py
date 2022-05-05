import math
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    dic = defaultdict()
    sell_dic = defaultdict(int)
    for e, r in zip(enroll, referral):
        dic[e] = r

    for s, a in zip(seller, amount):
        money = a * 100
        mine = money
        mine -= math.floor(money * (0.1))
        yours = math.floor(money * (0.1))

        sell_dic[s] += mine
        while dic[s] != "-" and yours != 0:
            s = dic[s]
            mine = yours - math.floor(yours * (0.1))
            yours = math.floor(yours * (0.1))
            sell_dic[s] += mine

    for name in enroll:
        answer.append(sell_dic[name])
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
