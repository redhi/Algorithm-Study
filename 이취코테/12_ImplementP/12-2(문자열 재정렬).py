S = list(input())
S.sort()

num = 0
count = 0
for i in range(len(S)):
    if 48<=ord(S[i])<=57: # 0~9 사이 숫자면
        num += int(S[i])
        count += 1
        
new_S = S[count:]
new_S.append(str(num))


print("".join(new_S))
