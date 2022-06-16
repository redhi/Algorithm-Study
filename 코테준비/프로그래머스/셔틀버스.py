def solution(n, t, m, timetable):
    answer = ""
    bus_time = [[9, 0]]

    visit = ["0"] * len(timetable)
    for _ in range(n - 1):
        h, minn = bus_time[-1]
        minn += t
        h += minn // 60
        minn = minn % 60
        bus_time.append([h, minn])
    bus_time_visit = ["0"] * len(bus_time)
    timetable.sort()

    for i in range(len(bus_time)):
        count = 0
        for j in range(len(timetable)):
            if visit[j] == "1":
                continue

            time = list(map(int, timetable[j].split(":")))
            bus_time_h, bus_time_m = bus_time[i]

            bus_time_mm = bus_time_h * 60 + bus_time_m
            time_h, time_m = time
            time_mm = time_h * 60 + time_m

            if time_mm <= bus_time_mm:
                count += 1
                visit[j] = "1"
            elif not i == len(bus_time) - 1:
                bus_time_visit[i] = "1"
                break

            if count >= m:
                bus_time_visit[i] = "1"
                break

    bus_time_visit = "".join(bus_time_visit)
    if bus_time_visit.rfind("0") == -1:
        visit = "".join(visit)
        find_idx = visit.find("0")
        if find_idx == -1:
            hh, mm = list(map(int, timetable[-1].split(":")))
        else:
            hh, mm = list(map(int, timetable[find_idx - 1].split(":")))

        if mm == 0:
            hh -= 1
            mm = 59
            answer = change_time(hh, mm)
        else:
            mm -= 1
            answer = change_time(hh, mm)
    else:
        find_idx = bus_time_visit.rfind("0")
        hh, mm = bus_time[find_idx]
        answer = change_time(hh, mm)

    return answer


def change_time(hh, mm):
    hh = str(hh)
    mm = str(mm)
    if len(hh) == 1:
        hh = "0" + hh
    if len(mm) == 1:
        mm = "0" + mm
    return hh + ":" + mm


n = 1
t = 1
m = 2
timetable = ["08:00", "08:01", "08:02", "08:03"]

print(solution(n, t, m, timetable))
