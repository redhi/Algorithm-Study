mylist1 = []
mylist2 = []

def CorrectType(line, mylist):
    if line.isalpha():
        print("",end="")
    else:
        mylist.append(float(line))
    
try:
    f1 = open("MP11Data1.txt")
except FileNotFoundError:
    print("MP11Data1.txt 파일이 존재하지 않습니다.")
else:
    lines = f1.readlines()
    for line in lines:
        line = line.strip()
        CorrectType(line, mylist1)
    f1.close()
    
try:
    f2 = open("MP11Data2.txt")
except FileNotFoundError:
    print("MP11Data2.txt 파일이 존재하지 않습니다.")
else:
    lines = f2.readlines()
    for line in lines:
        line = line.strip()
        CorrectType(line,mylist2)   
    f2.close()
    
least = 0
if(mylist1[-1]>=mylist2[-1]):
    least = mylist2[-1]
if(mylist1[-1]<mylist2[-1]):
    least = mylist1[-1]
    
print(len(mylist1))
print(len(mylist2))

num = 0
j = 0

for i in range(len(mylist1)+len(mylist2)):
    if(mylist1[j]>mylist2[num]):
        if(mylist1[j]==mylist1[-1]):
            print(mylist1[j])
            continue
        print(mylist1[j])
        j += 1
    elif(mylist1[j]==mylist2[num]):
        print(mylist1[j])
        print(mylist2[num])
        j += 1
        num += 1
    else:
        print(mylist2[num])
        if(mylist2[num]==mylist2[-1]):
            if(mylist2[num]==least):
                print(mylist2[num])
                break
            if(mylist1[j]==least):
                print(mylist1[j])
                break
            continue
        num += 1
        
