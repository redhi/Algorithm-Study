def solution(n, words):
    answer = []
    first = list(words[0])
    last_word = first[-1]
    count = 1
    person_count = 1
    person_num = 1
    for i in range(1, len(words)):
        word = list(words[i])
        if words[i] in words[:i]:
            # print("잉")
            person_count += 1
            # print(last_word, word[0], word, person_count, person_num)
            break

        if last_word == word[0]:
            if count + 2 == len(words):
                person_num = -1
                person_count = -1
                break
            last_word = word[-1]
            count += 1
            person_num += 1
            person_num %= n
            person_count = count // n
            print(person_count, person_num)
            # print(word)
        elif last_word != word[0]:
            print(person_count, person_num, count, word)
            break

            print(last_word, word[0], word, person_count, person_num)
    if person_num == 0:
        person_num += 1
    if person_num == -1:
        person_num += 1
    answer = [person_num, person_count + 1]
    # print(last_word, person_count + 1, count, person_num)

    return answer


n = 2
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# words = [
#     "hello",
#     "observe",
#     "effect",
#     "take",
#     "either",
#     "recognize",
#     "encourage",
#     "ensure",
#     "establish",
#     "hang",
#     "gather",
#     "refer",
#     "reference",
#     "estimate",
#     "executive",
# ]
# words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n, words))
