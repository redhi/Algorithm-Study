import sys

input = sys.stdin.readline


N, M = map(int, input().split())
# print(N, M)
city_route = [[] for _ in range(N + 1)]
# print(city_route)
for _ in range(M):
    A, B, C = map(int, input().split())
    city_route[A].append([B, C])

# print(city_route)
d = [100000001] * (N + 1)
d[1] = 0


def bellman(d, city_route):
    # print(len(city_route[1]))
    for _ in range(N):
        for i in range(N + 1):
            for j in range(len(city_route[i])):
                # print(city_route[i][j])
                arrive = city_route[i][j][0]
                wei = city_route[i][j][1]
                # print("i는", i, "j는 ", j, d[arrive], wei, d[i])
                if d[arrive] > d[i] + wei and not d[i] == 100000001:
                    d[arrive] = d[i] + wei
                # print(d)

    for i in range(N + 1):
        for j in range(len(city_route[i])):
            # print(city_route[i][j])
            arrive = city_route[i][j][0]
            wei = city_route[i][j][1]
            # print("i는", i, "j는 ", j, d[arrive], wei)
            # print(d)
            if d[arrive] > d[i] + wei and not d[i] == 100000001:
                return -1
                d[arrive] = d[i] + wei
    return d


# print(bellman(d, city_route))

d = bellman(d, city_route)

if d == -1:
    print(d)
else:
    for i in range(2, len(d)):
        if d[i] == 100000001:
            print(-1)
        else:
            print(d[i])
