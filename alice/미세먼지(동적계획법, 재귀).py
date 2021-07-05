N = int(input())
memo = []
def Tile(N):
    if N <= 1:
        return 1
    if N in memo:
        return memo[N]
    else:
        memo[N] = Tile(N-1) + Tile(N-2)
    return memo[N]
Tile = [1,1]
for i in range(2, N+1):
    Tile.append(Tile[i-1]+Tile[i-2])
    
print(Tile[-1]%10007)
