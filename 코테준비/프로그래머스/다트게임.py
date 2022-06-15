def solution(dartResult):
    answer = 0
    idx_list = []

    num_list = [[] for _ in range(len(dartResult))]
    for i in range(len(dartResult)):
        if dartResult[i] == "*":
            idx_list.append(["*", i])
        elif dartResult[i] == "#":
            idx_list.append(["#", i])
        elif dartResult[i].isdigit():
            if dartResult[i + 1].isdigit():
                num_list[i].append(dartResult[i : i + 2])
                num_list[i].append(dartResult[i + 2])
            else:
                num_list[i].append(dartResult[i])
                num_list[i].append(dartResult[i + 1])

    for idx in idx_list:
        if idx[0] == "#":
            num_list[idx[1] - 2].append("-")
        if idx[0] == "*":
            num_list[idx[1] - 2].append("*2")
            if idx[1] != 2:
                for i in range(idx[1] - 2 - 1, -1, -1):
                    if num_list[i]:
                        num_list[i].append("*2")
                        break

    for i in range(len(num_list)):
        tempnum = 0
        if num_list[i]:
            numm = int(num_list[i][0])
            if num_list[i][1] == "S":
                tempnum = numm ** 1
            if num_list[i][1] == "D":
                tempnum = numm ** 2
            if num_list[i][1] == "T":
                tempnum = numm ** 3
            for j in range(2, len(num_list[i])):
                if num_list[i][j] == "-":
                    tempnum *= -1
                if num_list[i][j] == "*2":
                    tempnum *= 2
            answer += tempnum

    return answer


dartResult = "1S2D*3T"
dartResult = "1D#2S*3S"
dartResult = "1D2S#10S"
print(solution(dartResult))
