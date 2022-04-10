import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    func1 = input().rstrip().replace("RR", "")
    func = func1.split("R")
    n = int(input())
    arr = input().rstrip()
    arr = arr.replace("[", "").replace("]", "").split(",")
    if arr == [""]:
        arr = []
    else:
        arr = deque(map(int, arr))

    if func1.count("D") > n:
        print("error")
        is_error = True
    elif func1.count("D") == n:
        print([])
        is_error = True
    elif arr == []:
        print([])
    else:
        front = True
        for i in range(len(func)):
            if len(func) == 1:
                front = True
            elif i != 0:
                if front == True:
                    front = False
                else:
                    front = True

            if front == True:
                for j in range(func[i].count("D")):
                    arr.popleft()
            else:
                for j in range(func[i].count("D")):
                    arr.pop()

        if (len(func) - 1) % 2 != 0:
            for k in range(0, len(arr), 2):
                arr[k // 2], arr[-(k // 2 + 1)] = arr[-(k // 2 + 1)], arr[k // 2]

        answer = "[" + ",".join(map(str, arr)) + "]"
        print(answer)
