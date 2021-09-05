'''03. 로그 파일 재정렬
Leetcode 937. Reorder Log Files'''

s = input()


def logsort(s):
    strfile = []
    numfile = []
    for i in s:
        if i.split()[1].isdigit():
            numfile.append(i.split())
        else:
            strfile.append(i.split())

    print(strfile, numfile)

    strfile = sorted(strfile, key=lambda x: (x[1:], x[0]))
    s = strfile+numfile
    new = []
    for i in range(len(s)):
        new.append(" ".join(s[i]))

    print(new)


def reorderLogFiles(logs):
    strfile = []
    numfile = []
    for i in logs:
        if i.split()[1].isdigit():
            numfile.append(i)
        else:
            strfile.append(i)
    strfile = sorted(strfile, key=lambda x: (x.split()[1:], x.split()[0]))
    newlog = strfile+numfile

    return newlog


logsort(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"])
logsort(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])
