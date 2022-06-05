from collections import defaultdict


def solution(N, stages):
    answer = []
    dic = defaultdict(int)
    stages.sort()
    for stage in stages:
        dic[stage] += 1
    summ = 0

    num = len(stages)
    for i in range(1, N + 1):
        now_num = num - summ
        n = dic.get(i)
        if n:
            answer.append([n / now_num, i])
        else:
            answer.append([0, i])
            n = 0
        summ += n

    answer.sort(key=lambda x: -x[0])
    answer2 = []
    for a in answer:
        answer2.append(a[1])

    return answer2


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
