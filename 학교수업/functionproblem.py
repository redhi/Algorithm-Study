def isLeapYear(year):
    if((year%4 == 0 and year%100 !=0) or year%400 == 0):
        return True
    else:
        return False
def getDayOfYear(year, month, day):
    if(year<=0):
       return 0
    if(not (1<=month and month<=12)):
       return 0
    if(month <= 2):
        return (month-1)*31+day
    else:
        return (month-1)*31+day+isLeapYear(year)-((4*month+23)//10)
    
year = int(input("년도를 입력하세요:"))
month = int(input("월을 입력하세요:"))
day = int(input("일을 입력하세요:"))
print("통일:",getDayOfYear(year,month,day))
