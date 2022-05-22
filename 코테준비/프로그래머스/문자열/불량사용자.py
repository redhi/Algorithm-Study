aa = []
bb = set()


def dfs(idx, n, banned_list):
    if len(aa) == n:
        aaa = sorted(aa)
        aaa = "".join(aaa)
        bb.add(aaa)
        return
    if idx > n:
        return
    for i in range(len(banned_list[idx])):
        if banned_list[idx][i] in aa:
            continue
        aa.append(banned_list[idx][i])
        dfs(idx + 1, n, banned_list)
        aa.pop()


def solution(user_id, banned_id):
    answer = 0

    banned_list = [set() for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            is_right = True
            if len(banned_id[i]) == len(user_id[j]):
                for k, z in zip(banned_id[i], user_id[j]):
                    if k == z:
                        continue
                    elif k == "*":
                        continue
                    else:
                        is_right = False
                        break
                if is_right:
                    banned_list[i].add(user_id[j])

    banned_list = list(map(list, banned_list))

    for i in range(len(banned_list[0])):
        dfs(0, len(banned_list), banned_list)

    answer = len(bb)

    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))
