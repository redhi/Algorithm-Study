import math

def inputFunc():
    my_list = []
    for i in range(5):
        figure = input()
        if(figure == "사각형"):
            my_list.append(figure)
            x1 = int(input("x1 좌표를 입력하시오:"))
            y1 = int(input("y1 좌표를 입력하시오:"))
            x2 = int(input("x2 좌표를 입력하시오:"))
            y2 = int(input("y2 좌표를 입력하시오:"))
            my_list.append((x1,y1,x2,y2))
            
        elif(figure == "삼각형"):
            my_list.append(figure)
            x1 = int(input("x1 좌표를 입력하시오:"))
            y1 = int(input("y1 좌표를 입력하시오:"))
            x2 = int(input("x2 좌표를 입력하시오:"))
            y2 = int(input("y2 좌표를 입력하시오:"))
            x3 = int(input("x3 좌표를 입력하시오:"))
            y3 = int(input("y3 좌표를 입력하시오:"))
            my_list.append((x1,y1,x2,y2,x3,y3))
            
        elif(figure == "원"):
            my_list.append(figure)
            x = int(input("x좌표를 입력하시오:"))
            y = int(input("y좌표를 입력하시오.:"))
            rad = int(input("반지름을 입력하시오.:"))
            my_list.append((x,y,rad))
            
    return my_list

def lengthFunc(my_tuple):
    crd = my_tuple
    num = (crd[0]-crd[4])**2 + (crd[1]-crd[5])**2
    return math.sqrt(num)

def areaFunc(my_list):
    j = 0
    for i in range(5):
        crd = my_list[j+1]
        if(my_list[j]=="사각형"):
            print("사각형")
            print("면적",(crd[2]-crd[0])*(crd[3]-crd[1]))
        elif(my_list[j]=="삼각형"):
            print("삼각형")
            print("면적",(crd[4]-crd[2])*lengthFunc(crd)/2)
        elif(my_list[j]=="원"):
            print("원")
            print("면적",(math.pi*(crd[2]**2)))
        j += 2
               
    
my_list = inputFunc()
areaFunc(my_list)
