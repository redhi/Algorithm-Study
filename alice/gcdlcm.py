a,b = map(int,input().split())

def gcd(a,b): # 유클리드 호제법 ; a%b와 b의 최대공약수와 a와 b의 최대공약수가 같다
    num1 = max(a,b) # 큰 값
    num2 = min(a,b) # 작은 값
    while num2>0:
        num1,num2=num2,num1%num2 # num1 = num2, num2 = num1%num2
    return num1

def lcm(a,b):
    return a*b/gcd(a,b)

print(int(lcm(a,b)))
