def solution(lottos, win_nums):
    answer = []
    count = 0
    win_dic = dict()
    for i in range(len(win_nums)):
        win_dic[win_nums[i]] = 1

    for j in range(len(lottos)):
        if win_dic.get(lottos[j]):
            count += 1
    extra = lottos.count(0)
    max_count = extra + count
    if max_count < 2:
        max_count = 1
    answer.append(7 - max_count)
    if count == 0:
        count = 1
    answer.append(7 - count)

    return answer


lottos = [44, 1, 0, 0, 31, 25]
lottos = [7, 2, 3, 4, 5, 0]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
