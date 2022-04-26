def solution(gems):
    answer = [0, len(gems) - 1]
    gems_set_num = len(list(set(gems)))
    gems_dic = {gems[0]: 1}
    n = len(gems)
    s, e = 0, 0
    while s < n and e < n:
        if len(gems_dic) < gems_set_num:
            e += 1
            if e == n:
                break
            gems_dic[gems[e]] = gems_dic.get(gems[e], 0) + 1

        else:
            if (e - s) < (answer[1] - answer[0]):
                answer[0], answer[1] = s, e

            if gems_dic[gems[s]] == 1:
                del gems_dic[gems[s]]
            elif gems_dic[gems[s]] > 1:
                gems_dic[gems[s]] -= 1
            s += 1

    answer[0] += 1
    answer[1] += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
