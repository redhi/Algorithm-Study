"""
프로그래머스 디스크 컨트롤러
1. 현재 시점에서 가장 소요시간 작은 순으로 작업
2. 현재 시점 - 요청 시간 = 대기 시간
"""


def solution(jobs):
    answer, now = 0, 0

    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) != 0:
        for i in range(len(jobs)):

            if jobs[i][0] <= now:
                now += jobs[i][1]
                answer += now - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                now += 1

    return answer // length
