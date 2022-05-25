# 단어 뒤집기 2

import sys

input = sys.stdin.readline
words = input().rstrip()
print(words)
words = words.split(">")
print(words)
word_str = ""
for word in words:
    if word:
        if word[0] == "<":
            word_str += word + ">"
        else:
            if word.count("<") > 0:
                a, b = word.split("<")
                word_str += a[::-1]
                word_str += "<" + b + ">"
            else:
                word_str += word[::-1]
    print(word_str)
# .replace("<", ",").replace(">", ",")
