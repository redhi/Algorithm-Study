import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

if len(bomb) > len(s):
    print(s)
else:
    stack = []
    for i in range(len(s)):
        if len(stack) >= len(bomb):
            if "".join(stack[-len(bomb) :]) == bomb:
                for j in range(len(bomb)):
                    stack.pop()
        stack.append(s[i])
    if "".join(stack[-len(bomb) :]) == bomb:
        for j in range(len(bomb)):
            stack.pop()

    s = "".join(stack)
    if s == "":
        print("FRULA")
    else:
        print(s)
