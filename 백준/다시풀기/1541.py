"""
백준 잃어버린 괄호
"""

N = input().split("-")

result = []

for i in N:
    num = list(map(int, i.split("+")))
    result.append(sum(num))

for i in range(len(result)):
    if i == 0:
        answer = result[0]
    else:
        answer -= result[i]

print(answer)
