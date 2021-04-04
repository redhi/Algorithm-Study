year = int(input("년도를 입력하세요:"))
month = int(input("월을 입력하세요:"))
day = int(input("일을 입력하세요:"))
count =0
if((year%4 == 0 and year%100 !=0) or year%400 == 0):
    count = count+1
if(month <= 2):
          dayofYear = (month-1)*31+day
else:
    dayofYear = (month-1)*31+day+count-((4*month+23)//10)
print("통일:",dayofYear)
