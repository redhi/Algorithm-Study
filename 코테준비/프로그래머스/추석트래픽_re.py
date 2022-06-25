def solution(lines):
    answer = 0
    log_info = []
    for i in lines:
        info = i.split(" ")
        time = list(map(float, info[1].split(":")))
        spent_time = float(info[2].replace("s", ""))
        h, m, s = time
        ss = (h * 60 + m) * 60 + s

        start_s = ss - spent_time + 0.001
        start_s = round(start_s, 3)
        end_s = ss

        log_info.append([start_s, end_s])

    log_info.sort(key=lambda x: (x[0], x[1]))

    for log in log_info:
        answer = max(
            answer,
            check(log_info, log[0], log[0] + 1),
            check(log_info, log[1], log[1] + 1),
        )

    return answer


def check(log_info, start, end):
    count = 0
    for log in log_info:
        if log[0] < end and log[1] >= start:
            count += 1
    return count


lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s",
]
# lines = ["2016-09-15 23:59:59.999 0.001s"]
# lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
print(solution(lines))
