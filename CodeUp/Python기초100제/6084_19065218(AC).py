h,b,c,s = map(int,input().split())
result = h*b*c*s/8/1024/1024
print(round(result,1),"MB") #round(n,1) 소수점 첫째자리까지 반올림

