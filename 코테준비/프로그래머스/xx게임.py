max_num = 0
def solution(k, dungeons):
    global max_num
    dfs(k, 0, dungeons)

    return max_num


visit = [0 for _ in range(9)]
a = []


def dfs(k, count, dungeons):
    global max_num
    if len(a) == len(dungeons):
        answer = 0
        for i in a:
            limit, spent = dungeons[i]
            if k >= limit:
                k -= spent
                answer += 1
        max_num = max(max_num, answer)
        return
    for i in range(len(dungeons)):
        if visit[i] == 1:
            continue
        if visit[i] == 0:
            visit[i] = 1
            a.append(i)
            dfs(k, count + 1, dungeons)
            a.pop()
            visit[i] = 0


dungeons = [[80, 20], [50, 40], [30, 10]]

k = 80
solution(k, dungeons)

print("정답", max_num)
