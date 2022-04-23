from collections import defaultdict


def solution(genres, plays):
    answer = []
    g_list = defaultdict(list)
    g_int = defaultdict(int)

    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        g_list[g].append([p, i])
        g_int[g] += p

    many_list = [i[0] for i in sorted(g_int.items(), key=lambda x: x[1], reverse=True)]

    for key in many_list:
        g_list[key].sort(key=lambda x: (-x[0], x[1]))
        if len(g_list[key]) < 2:
            answer.append(g_list[key][0][1])
        else:
            answer.append(g_list[key][0][1])
            answer.append(g_list[key][1][1])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
