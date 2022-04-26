def solution(play_time, adv_time, logs):

    p_h, p_m, p_s = map(int, play_time.split(":"))
    play_time = (p_h * 60 + p_m) * 60 + p_s

    a_h, a_m, a_s = map(int, adv_time.split(":"))
    adv_time = (a_h * 60 + a_m) * 60 + a_s

    all_time = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = log.split("-")
        s_h, s_m, s_s = map(int, start.split(":"))
        e_h, e_m, e_s = map(int, end.split(":"))
        ss = (s_h * 60 + s_m) * 60 + s_s
        ee = (e_h * 60 + e_m) * 60 + e_s
        for i in range(ss, ee):
            all_time[i] += 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    h = max_time // 3600
    m = (max_time % 3600) // 60
    s = (max_time % 3600) % 60
    h, m, s = str(h), str(m), str(s)
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s

    return h + ":" + m + ":" + s


play_time = "02:03:55"
adv_time = "00:14:15"
logs = [
    "01:20:15-01:45:14",
    "00:40:31-01:00:00",
    "00:25:50-00:48:29",
    "01:30:59-01:53:29",
    "01:37:44-02:02:30",
]
print(solution(play_time, adv_time, logs))
