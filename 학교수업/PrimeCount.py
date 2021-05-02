def readNumber():
    num = int(input("정수 한 개를 입력하세요:"))
    while(num<2):
        print("2 이상의 숫자를 입력하라")
        num = int(input("정수 한 개를 입력하세요:"))
    return num

def getCountsOfDivisors(num):
    a = 1
    Dnum = 0
    while(a<=num):
        if(num%a==0):
            Dnum += 1
        a += 1
    return Dnum

def isPrime(num):
    a = getCountsOfDivisors(num)
    if(a==2):
        return True
    else:
        return False
        
a = readNumber()
print("정수:",a,"약수 개수:",getCountsOfDivisors(a),"소수:",isPrime(a))

