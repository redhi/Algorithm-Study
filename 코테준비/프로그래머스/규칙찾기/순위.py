from collections import defaultdict


def solution(n, results):
    answer = 0
    winner_list = defaultdict(set)
    loser_list = defaultdict(set)

    for winner, loser in results:
        winner_list[loser].add(winner)
        loser_list[winner].add(loser)

    for i in range(1, n + 1):
        for winner in winner_list[i]:
            loser_list[winner].update(loser_list[i])
        for loser in loser_list[i]:
            winner_list[loser].update(winner_list[i])

    for i in range(1, n + 1):
        if (len(winner_list[i]) + len(loser_list[i])) == (n - 1):
            answer += 1

    return answer
