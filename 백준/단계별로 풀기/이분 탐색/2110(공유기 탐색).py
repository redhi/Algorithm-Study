import sys
N, C = map(int, (input().split()))
home = [int(sys.stdin.readline()) for _ in range(N)]

def routercount(distance):
    count = 1
    cur_home = home[0] 
    for i in range(1, N):
        if cur_home + distance <= home[i]:
            cur_home = home[i]
            count += 1
    return count

home = sorted(home)
start, end = 1, home[-1] - home[0]

while start <= end:
    mid = (start+end) // 2
    
    if routercount(mid) >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)
