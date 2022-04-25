import sys

input = sys.stdin.readline

t = int(input().rstrip())

day = {"MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1, "SUN": 7}
arr = [input().rstrip() for _ in range(t)]
for a in range(len(arr)):
    print("#" + str(a), day.get(arr[a]))
