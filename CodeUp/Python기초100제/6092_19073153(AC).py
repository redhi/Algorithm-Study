n = int(input())
a = input().split() # 여러 개를 입력하여 저장하면 리스트의 형태로 str로 저장

for i in range(n):
    a[i] = int(a[i])

score = []
for i in range(24):
    score.append(0)

for i in range(n):
    score[a[i]] += 1
for i in range(1,24):
    print(score[i], end=' ')
