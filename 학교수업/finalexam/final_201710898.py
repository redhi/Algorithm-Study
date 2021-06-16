import sys

def readFile(filename):
    mylist1 = []
    try:
        f1 = open(filename,'rt',encoding= "UTF-8")
    except FileNotFoundError:
        print(filename,"파일이 존재하지 않습니다.")
    except IOError:
        f1 = open(filename)
    else:
        lines = f1.readlines()
        for line in lines:
            line = line.strip()
            mylist1.append(list(line))
        f1.close()
    return mylist1

def updateDictionary(dic, lines):
    dic = dict()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            dic[lines[i][j]]= dic.get(lines[i][j],0) +1 
    return dic

def printDictionary(dic, letter):
    if letter == "A" or letter == "a":
        for key,value in dic.items():
            if key.isalpha():
                print(key, value)
        
    if letter == "D" or letter == "d":
        for key,value in dic.items():
            if key.isdigit():
                print(key, value)
        
    if letter == "W" or letter == "w":
        for key,value in dic.items():
            if key.isspace():
                print(key, value)
        

    if letter == "E" or letter == "e":
        for key,value in dic.items():
            if key.isalpha() or key.isspace() or key.isdigit():
                print("",end="")
            else:
                print(key, value)       

    sys.exit()
    
class MYDICT:
    def __init__(self, filename):
        self.filename = filename
        
    def readFile(self):
        mylist1 = []
        try:
            f1 = open(self.filename,'rt',encoding= "UTF-8")
        except FileNotFoundError:
            print(filename,"파일이 존재하지 않습니다.")
        except IOError:
            print("---")
            f1 = open(self.filename)
        else:
            lines = f1.readlines()
            for line in lines:
                line = line.strip()
                mylist1.append(list(line))
            f1.close()
        print(len(mylist1))
        return mylist1

    def updateDictionary(dic, lines):
        dic = dict()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                dic[lines[i][j]]= dic.get(lines[i][j],0) +1 
        return dic

    def printDictionary(dic, letter):
        if letter == "A" or letter == "a":
            for key,value in dic.items():
                if key.isalpha():
                    print(key, value) 
        if letter == "D" or letter == "d":
            for key,value in dic.items():
                if key.isdigit():
                    print(key, value)  
        if letter == "W" or letter == "w":
            for key,value in dic.items():
                if key.isspace():
                    print(key, value)
        if letter == "E" or letter == "e":
            for key,value in dic.items():
                if key.isalpha() or key.isspace() or key.isdigit():
                    print("",end="")
                else:
                    print(key, value)       

        sys.exit()
MYDICT1 = MYDICT("python.txt")
my_list = readFile("python.txt")
my_dic = dict()
my_dic = updateDictionary(my_dic, my_list)
my_str = input("A, D, W, E 중 한 글자를 입력하세요(대문자와 소문자 가능):")
printDictionary(my_dic, my_str)

