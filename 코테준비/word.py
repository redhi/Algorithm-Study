"""
프로그래머스 단어변환
"""


answer = 0
is_end = 0


def solution(begin, target, words):
    visit = [0] * len(words)
    global answer

    for i in range(len(words)):
        if words[i] == target:
            visit[i] = 1
    dfs(visit, begin, target, words, target)

    return answer


def dfs(visit, begin, target, words, word):
    global is_end
    global answer

    if not target in words:
        return
    if word == begin:
        return
    for i in range(len(words)):
        w = list(word)
        s = list(begin)
        if visit[i] == 0:
            count = 0
            b_count = 0
            for j in range(len(w)):
                if w[j] == s[j]:
                    b_count += 1

                if w[j] == words[i][j]:
                    count += 1

            if b_count == (len(w) - 1):
                answer += 1
                is_end = 1
                break

            elif count == (len(w) - 1):
                visit[i] = 1
                if is_end != 1:
                    answer += 1
                dfs(visit, begin, target, words, words[i])


begin = "hit"
target = "cog"
words = ["hot", "dot", "cog"]
print(solution(begin, target, words))
