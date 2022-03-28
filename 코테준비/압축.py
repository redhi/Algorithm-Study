def solution(msg):
    answer = []
    dict = {}
    for i in range(ord("A"), ord("Z") + 1):
        dict[chr(i)] = i - 64
    msg = list(msg)
    next = 0
    for i in range(len(msg)):
        if next == i:
            for j in range(i + 1, len(msg) + 1):
                dict_value = dict.get("".join(msg[i:j]))
                if dict_value:
                    if j == len(msg):
                        answer.append(dict_value)
                else:
                    answer.append(dict.get("".join(msg[i : j - 1])))
                    next = j - 1
                    dict["".join(msg[i:j])] = len(dict) + 1
                    break

    return answer


msg = "KAKAO"
# msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))
