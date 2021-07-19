N = list(map(int, input()))
num1 = 0
num2 = 0

for i in range(0,(len(N)//2)): # 앞부분
    num1 += N[i]

for j in range(len(N)//2, len(N)): # 뒷부분
    num2 += N[j]

if num1 == num2:
    print("LUCKY")
else:
    print("READY")
