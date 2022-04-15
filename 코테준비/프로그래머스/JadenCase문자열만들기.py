def solution(s):
    answer = []

    s = s.split(" ")
    for i in range(len(s)):
        pre_str = list(s[i])
        for j in range(len(pre_str)):
            if j == 0 and pre_str[j].isalpha():
                strr = pre_str[j]
                pre_str[j] = strr.upper()
            elif pre_str[j].isalpha():
                pre_str[j] = pre_str[j].lower()
        answer.append("".join(pre_str))

    answer = " ".join(answer)
    return answer


s = "3people unFollowed me"

print(solution(s))
