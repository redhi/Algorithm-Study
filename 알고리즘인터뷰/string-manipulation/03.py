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

    strfile = sorted(strfile, key=lambda x: (x[1], x[0]))
    newlogfile = strfile+numfile

    print(newlogfile)


logsort(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"])
