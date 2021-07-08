N, M = map(int, input().split())
my_board = list()

for i in range(N):
    my_board.append(input())
repair_mini = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k + l) % 2 == 0:
                    if my_board[k][l] != 'W':
                        first_W = first_W+1
                    if my_board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if my_board[k][l] != 'B':
                        first_W = first_W+1
                    if my_board[k][l] != 'W':
                        first_B = first_B + 1
        repair_mini.append(first_W)
        repair_mini.append(first_B)
print(min(repair_mini))
