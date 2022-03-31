def solution(record):
    answer = []
    uid = {}

    for r in record:
        info_info = r.split(" ")
        if info_info[0] == "Enter" or info_info[0] == "Change":
            uid[info_info[1]] = info_info[2]
    for r in record:
        info_info = r.split(" ")
        if info_info[0] == "Enter":
            nickname = uid.get(info_info[1])
            answer.append(nickname + "님이 들어왔습니다.")

        if info_info[0] == "Leave":
            nickname = uid.get(info_info[1])
            answer.append(nickname + "님이 나갔습니다.")

    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
print(solution(record))
