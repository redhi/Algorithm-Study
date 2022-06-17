def solution(N, stages):
    answer = []
    stage_r = []
    stage_rate = [[] for _ in range(N + 2)]

    for i in stages:
        stage_rate[i].append(i)

    for i in range(1, N + 2):
        new = []
        for j in range(i, N + 2):
            new += stage_rate[j]
        if not i == N + 1:
            chall_num = len(new)
            not_pass_num = len(stage_rate[i])
            if chall_num == 0:
                stage_r.append([0, i])
            else:
                stage_r.append([not_pass_num / chall_num, i])

    stage_r.sort(key=lambda x: (-x[0], x[1]))
    for i in range(len(stage_r)):
        answer.append(stage_r[i][1])

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 3
stages = [1, 1, 1]
# stages = [4, 4, 4, 4, 4]
print(solution(N, stages))
