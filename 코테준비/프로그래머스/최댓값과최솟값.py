def solution(s):
    answer = ""
    s = list(map(int, s.split(" ")))
    # print(s)
    # print(min(s), max(s))
    answer = str(min(s)) + " " + str(max(s))
    return answer
