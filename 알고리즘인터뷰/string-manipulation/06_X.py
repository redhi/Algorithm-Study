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


class Solution:
    def isPalindrome(self, in_str: str) -> bool:
        count = 0
        #in_str = in_str.replace(" ", "")
        in_str = ''.join(char for char in in_str if char.isalnum())  # 특수문자제거
        in_str = in_str.lower()

        for i in range(len(in_str)//2):
            if in_str[i] == in_str[-(i+1)]:
                #print(in_str[i], in_str[-(i+1)])
                count += 1

        if count == (len(in_str)//2):
            return True
        return False


def isPalindrome(mystr):
    def expand(left, right):
        while left >= 0 and right < len(mystr) and mystr[left] == mystr[right]:
            left -= 1
            right += 1
        return mystr[left+1:right]
    if len(mystr) < 2 or mystr == mystr[::-1]:
        return mystr


isPalindrome("")
