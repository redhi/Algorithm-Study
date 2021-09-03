in_str = input()


def check(in_str):
    count = 0
    #in_str = in_str.replace(" ", "")
    in_str = ''.join(char for char in in_str if char.isalnum())  # 특수문자제거
    in_str = in_str.lower()

    for i in range(len(in_str)//2):
        if in_str[i] == in_str[-(i+1)]:
            #print(in_str[i], in_str[-(i+1)])
            count += 1

    if count == (len(in_str)//2):
        return "true"
    return "false"


print(check(in_str))


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
