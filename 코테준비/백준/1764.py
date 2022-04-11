import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
for i in range(n):
    name = input().rstrip()
    dic[name] = 1
answer = []
count = 0
for j in range(m):
    name = input().rstrip()
    if dic.get(name) == 1:
        count += 1
        answer.append(name)
print(count)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
