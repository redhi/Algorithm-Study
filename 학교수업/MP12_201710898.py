import math

class Distance:
    @staticmethod
    def getDistance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
class Triangle:
    def __init__(self, coords):
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = coords[2]
        self.y2 = coords[3]
        self.x3 = coords[4]
        self.y3 = coords[5]
    def getArea(self):
        length1 = Distance.getDistance(self.x1, self.y1, self.x2, self.y2)
        length2 = Distance.getDistance(self.x1, self.y1, self.x3, self.y3)
        length3 = Distance.getDistance(self.x3, self.y3, self.x2, self.y2)
        s = (length1+length2+length3)/2
        area = math.sqrt(s*(s-num1)*(s-num2)*(s-num3))
        return area
    
class Circle:
    def __init(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.rad = coords[2]
    def getArea(self):
        return math.pi*(self.rad**2)
class Rectangle:
    def __init__(self, coords):
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = coords[2]
        self.y2 = coords[3]

    def getArea(self):
            width = Distance.getDistance(self.x2, self.y1, self.x1, self.y1)
            height = Distance.getDistance(self.x1, self.y2, self.x1, self.y1)
            return width * height

def readLines(filename):
    f = open(filename)
    lines = f.readlines()
    return lines

def readCoordinates(lines, idx, n):
    t1 = ()
    #print(n)
    for i in range(n):
        coordinate = int(lines[idx].strip())
        idx += 1
        t1 = t1 + (coordinate,)
    return t1

def getShapesInfos(lines):
    index = 0
    lst = []
    for i in range(5):
        shapeType = lines[index].strip()
        index += 1
        lst.append(shapeType)
        t1 = ()
        if shapeType == "사각형":
            t1 = readCoordinates(lines, index, 4)
            index += 4

        elif shapeType == "삼각형":
            t1 = readCoordinates(lines, index, 6)
            index += 6           

        elif shapeType == "원":
            t1 = readCoordinates(lines, index, 3)
            index += 3           

        lst.append(t1)
    print("\n", lst)
    return lst


def calcRectangleArea(t):
    r = Rectangle(t)
    return r.getArea()


def calcTriangleArea(t):
    a = Distance.getDistance(t[4], t[5], t[2], t[3])
    b = Distance.getDistance(t[4], t[5], t[0], t[1])
    c = Distance.getDistance(t[2], t[3], t[0], t[1])
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calcCircleArea(t):
    return math.pi * t[2] * t[2]

lst = readLines("MP09data.txt")
"""
for line in lst:
    line = line.strip()
    print(line)
"""

l = getShapesInfos(lst)

area = 0
for i in range(0, 10, 2):
    if l[i] == "사각형":
        area = calcRectangleArea(l[i + 1])
    elif l[i] == "삼각형":
        area = calcTriangleArea(l[i + 1])
    elif l[i] == "원":
        area = calcCircleArea(l[i + 1])
    print(l[i]) # 도형
    print("면적: ", area)
