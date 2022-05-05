from collections import deque


def solution(jobs):
    answer = 0
    job_list = []
    for job in jobs:
        start, spent = job
        job_list.append([start, spent, start + spent])
    # print(job_list)
    job_list.sort(key=lambda x: (x[2], x[0]))
    # print(job_list)
    job_list = deque(job_list)
    now = 0
    start, spent, cer = job_list.popleft()
    now += start + spent
    spent_list = []
    spent_list.append(now - start)
    while job_list:
        start, spent, cer = job_list.popleft()
        if start <= now:
            now += spent
        else:
            job_list.append([start, spent, cer])
            job_list.sort(key=lambda x: (x[0]))
            start, spent, cer = job_list.popleft()
            if start <= now:
                now += spent
            else:
                s = start - now
                now += s + spent
            job_list.sort(key=lambda x: (x[2], x[0]))
        spent_list.append(now - start)
    # print(spent_list)
    answer = sum(spent_list) // len(spent_list)

    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
