count = 0


def solution(s):
    global count
    answer = []
    zero_count = 0

    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0", "")
        s_len = len(s)
        s = con(s_len)

    answer.append(count)
    answer.append(zero_count)

    return answer


def con(s_len):
    global count
    next = s_len
    next_result = s_len
    result = []
    while next != 0:
        next_result = next % 2
        next //= 2
        result.append(next_result)
    result.sort(reverse=True)

    count += 1
    return "".join(map(str, result))


s = "110010101001"

print(solution(s))
