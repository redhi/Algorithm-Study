import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
arr[0][0] = 1

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = 2

l = int(input())

t_dict = {}
for _ in range(l):
    s, c = input().rstrip().split()
    t_dict[int(s)] = c
move_dic = {"UP": [0, 1], "RIGHT": [1, 0], "DOWN": [0, -1], "LEFT": [-1, 0]}
rot_dic = {
    "UP": {"L": "LEFT", "D": "RIGHT"},
    "RIGHT": {"L": "UP", "D": "DOWN"},
    "DOWN": {"L": "RIGHT", "D": "LEFT"},
    "LEFT": {"L": "DOWN", "D": "UP"},
}

time = 0
y, x = 0, 0
dire = "UP"
t_y, t_x = 0, 0

sneak = deque()
sneak.append((y, x))
while True:
    time += 1
    d_y, d_x = move_dic[dire]
    now_y = y + d_y
    now_x = x + d_x

    if 0 <= now_y < n and 0 <= now_x < n:
        if arr[now_y][now_x] == 0:
            arr[now_y][now_x] = 1
            sneak.append((now_y, now_x))
            t_y, t_x = sneak.popleft()
            arr[t_y][t_x] = 0
            y = now_y
            x = now_x
        elif arr[now_y][now_x] == 2:
            arr[now_y][now_x] = 1
            sneak.append((now_y, now_x))
            y = now_y
            x = now_x
        else:
            break
    else:
        break

    if t_dict.get(time):
        dire = rot_dic[dire][t_dict.get(time)]


print(time)
