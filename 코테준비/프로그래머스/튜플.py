def solution(s):
    answer = []
    s = s.split("},")
    arr = []
    for i in range(len(s)):
        pre_s = s[i].replace("{", "").replace("}", "")
        pre_s = list(map(int, pre_s.split(",")))
        arr.append(pre_s)

    arr.sort(key=lambda x: len(x))
    answer.append(arr[0][0])
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in answer:
                continue
            answer.append(arr[i][j])

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
