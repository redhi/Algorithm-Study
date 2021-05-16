import math

def areaFunc(my_list):
    j = 0
    for i in range(5):
        crd = my_list[j+1]
        if(my_list[j]=="사각형"):
            print("사각형")
            num1 = (crd[0]-crd[0])**2+(crd[3]-crd[1])**2
            num1 = math.sqrt(num1)
            num2 = (crd[2]-crd[0])**2+(crd[1]-crd[1])**2
            num2 = math.sqrt(num2)
            print("면적",num1*num2)
        elif(my_list[j]=="삼각형"):
            print("삼각형")
            num1 = (crd[0]-crd[2])**2 + (crd[1]-crd[3])**2
            num1 = math.sqrt(num1)
            num2 = (crd[2]-crd[4])**2 + (crd[3]-crd[5])**2
            num2 = math.sqrt(num2)
            num3 = (crd[4]-crd[0])**2 + (crd[1]-crd[5])**2
            num3 = math.sqrt(num3)
            s = (num1+num2+num3)/2
            area = math.sqrt(s*(s-num1)*(s-num2)*(s-num3))
            print("면적",area)
        elif(my_list[j]=="원"):
            print("원")
            print("면적",(math.pi*(crd[2]**2)))
        j += 2
               
f = open("MP09data.txt")

my_list = []
line = f.readline()
while line:
    line = line.strip()
    if(line == "사각형"):
            my_list.append(line)
            x1 = f.readline()
            x1 = int(x1.strip())
            y1 = f.readline()
            y1 = int(y1.strip())
            x2 = f.readline()
            x2 = int(x2.strip())
            y2 = f.readline()
            y2 = int(y2.strip())
            my_list.append((x1,y1,x2,y2))
            
    elif(line == "삼각형"):
            my_list.append(line)
            x1 = f.readline()
            x1 = int(x1.strip())
            y1 = f.readline()
            y1 = int(y1.strip())
            x2 = f.readline()
            x2 = int(x2.strip())
            y2 = f.readline()
            y2 = int(y2.strip())
            x3 = f.readline()
            x3 = int(x3.strip())
            y3 = f.readline()
            y3 = int(y3.strip())
            my_list.append((x1,y1,x2,y2,x3,y3))
            
    elif(line == "원"):
            my_list.append(line)
            x = f.readline()
            x = int(x.strip())
            y = f.readline()
            y = int(y.strip())
            rad = f.readline()
            rad = int(rad.strip())
            my_list.append((x,y,rad))
    line = f.readline()


f.close()
areaFunc(my_list)
