# 단어 뒤집기 2

import sys

input = sys.stdin.readline
words = input().rstrip()
words = words.split(">")

word_str = ""
for word in words:
    if word:
        if word[0] == "<":
            word_str += word + ">"
        else:
            if word.count("<") > 0:
                a, b = word.split("<")
                a_list = a.split()
                for idx, aa in enumerate(a_list):
                    word_str += aa[::-1]
                    if idx != len(a_list) - 1:
                        word_str += " "
                word_str += "<" + b + ">"
            else:
                a_list = word.split()
                for idx, aa in enumerate(a_list):
                    word_str += aa[::-1]
                    if idx != len(a_list) - 1:
                        word_str += " "

print(word_str)
