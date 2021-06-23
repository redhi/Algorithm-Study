oper = input().split('-')
result = 0

for i in oper[0].split('+'):
    result += int(i)

for i in oper[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
