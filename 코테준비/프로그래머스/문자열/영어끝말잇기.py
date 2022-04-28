from collections import defaultdict


def solution(n, words):
    word_dict = defaultdict(int)
    stack = []
    for idx, word in enumerate(words):
        person_num = idx % n + 1
        round_num = idx // n + 1
        if word_dict.get(word):
            answer = [person_num, round_num]
            return answer
        else:
            if stack:
                if stack[-1][-1] == word[0]:
                    word_dict[word] += 1
                    stack.append(word)
                else:
                    answer = [person_num, round_num]
                    return answer
            else:
                stack.append(word)
                word_dict[word] += 1

    return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))
