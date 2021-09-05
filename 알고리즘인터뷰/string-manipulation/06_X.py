'''
06 가장 긴 팰린드롬 부분 문자열(미완)
leetcode 5. Longest Palindrome Substring
'''
strs = input()


def palindrome(strs):
    strs = list(strs)
    re_strs = strs
    re_strs = strs[::-1]  # 뒤집어서 집어넣음
    count = 0
    num = []
    for i in range(len(strs)):  # 최대 팰린드롬 길이 구함

        if strs[i] == re_strs[i]:
            print(strs[i], "뒤집힌", re_strs[i])
            count += 1
            num.append(count)
        else:
            count = 0
            num.append(count)
        print(num)
    result = []
    for i in range(len(strs)):

        if num[i] == 0:
            result.append(" ")
        else:
            result.append(strs[i])
        print(result)


# new = []
# new = strs[i:]
# re_new = new
# re_new.reverse()
# print("응?", new)
# print(re_new)
# abbdbdbdbbc
# cbbdbdbdbba


palindrome(strs)
