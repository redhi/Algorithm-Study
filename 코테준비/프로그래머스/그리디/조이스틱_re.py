def solution(name):
    answer = 0

    name = list(name)

    num_list = []
    min_move = len(name) - 1
    for n in range(len(name)):
        num = abs(ord(name[n]) - ord("A"))
        num = min(num, 26 - num)
        answer += num
        num_list.append(num)
        next = n + 1
        while next < len(name) and name[next] == "A":
            next += 1
        # print(next, n)
        min_move = min(min_move, 2 * n + len(name) - next, n + 2 * (len(name) - next))
    answer += min_move

    return answer


name = "JEROEN"
# name = "JAZ"
name = "JAN"
# name = "JAZZZA"
# name = "JAAN"
name = "JAANAABAA"
name = "BAAABAAAAAAAAAAAAAAAAAB"
name = "ABAAB"
# 2 + 5 - 4
# 16+N
# 9+13+13
# 26+9 = 35
print(solution(name))
