from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    an = defaultdict(int)
    report_per = defaultdict(set)
    bad_user = defaultdict(int)
    bad_user_reporter = defaultdict(set)
    for id in id_list:
        report_per[id].update()
        bad_user[id] = 0
        an[id] = 0
        bad_user_reporter[id].update()
    for re in report:
        a, b = re.split(" ")
        report_per[a].add(b)
    for id in id_list:
        for i in report_per[id]:
            bad_user[i] += 1
            bad_user_reporter[i].add(id)

    for id in id_list:
        if bad_user[id] >= k:
            ree = list(bad_user_reporter[id])
            for i in range(len(ree)):
                an[ree[i]] += 1

    for id in id_list:
        answer.append(an[id])

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
report = [
    "muzi frodo",
    "muzi frodo",
    "apeach frodo",
    "frodo neo",
    "muzi neo",
    "apeach muzi",
]
k = 2

print(solution(id_list, report, k))
