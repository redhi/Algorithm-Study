def solution(s):
    answer = int(1e9)
    n = len(s) // 2

    if len(s) == 1:
        return 1
    for i in range(1, n + 1):
        ss = ""
        count = 1
        for j in range(i, len(s), i):
            if s[j - i : j] == s[j : j + i]:
                count += 1
                if j + i >= len(s):
                    ss += str(count) + s[j - i : j]
            else:

                if count != 1:
                    ss += str(count) + s[j - i : j]
                else:
                    ss += s[j - i : j]
                if j + i >= len(s):
                    ss += s[j:]

                count = 1

        answer = min(answer, len(ss))
    return answer


print(solution("a"))
