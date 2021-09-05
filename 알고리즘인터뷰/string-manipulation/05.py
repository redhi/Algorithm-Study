'''
05 그룹 애너그램
leetcode 49. Group Anagrams
'''
s = input()


def anagrams(s):
    sort_word = []
    for w in s:
        sort_word.append(''.join(sorted(list(w))))  # 문자 정렬

    word_dict = {}
    for i in range(len(sort_word)):
        num = []
        if sort_word[i] not in word_dict:  # 없는 값 딕셔너리에 추가
            num.append(i)
            word_dict[sort_word[i]] = num
        else:
            num = word_dict.get(sort_word[i])  # 있는 값이면 list로 추가
            num.append(i)
            word_dict[sort_word[i]] = num

    result = []
    for num in word_dict.values():  # 딕셔너리 값 배열 ex) [0,1,3]
        sub = []
        for n in num:
            sub.append(s[n])  # 애너그램이 일치하는 리스트 추가
        result.append(sub)  # 전체 배열에 추가

    print(result)


#anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bats'])
anagrams(s)


def groupAnagrams(strs):
    sort_word = []
    for w in strs:
        sort_word.append(''.join(sorted(list(w))))
    # print(sort_word)

    word_dict = {}
    for i in range(len(sort_word)):
        num = []
        if sort_word[i] not in word_dict:  # 없는 값 딕셔너리에추가
            num.append(i)
            word_dict[sort_word[i]] = num
        else:
            num = word_dict.get(sort_word[i])  # 있는 값이면list로 추가
            num.append(i)
            word_dict[sort_word[i]] = num

    # print(word_dict)

    result = []
    for num in word_dict.values():
        sub = []
        # print(num)
        for n in num:
            # print(n)
            sub.append(strs[n])
        result.append(sub)

    return result
