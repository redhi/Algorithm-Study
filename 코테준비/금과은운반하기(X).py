def solution(a, b, g, s, w, t):
    answer = -1
    time = 0
    not_full = True
    aa = 0
    bb = 0

    while not_full:
        for i in range(len(g)):
            if ((time - t[i]) % (2 * t[i])) == 0:
                # print(g[i])
                if g[i] != 0 and aa < a:
                    if a - aa < w[i]:
                        n = a - aa
                        aa += n
                        left = w[i] - n
                        s[i] -= left

                        bb += left

                    elif g[i] < w[i]:
                        aa += g[i]
                        left = w[i] - g[i]
                        s[i] -= left
                        bb += left
                        g[i] = 0
                    else:
                        aa += w[i]
                        g[i] -= w[i]
                else:
                    if s[i] < w[i]:
                        bb += s[i]
                        s[i] = 0
                    else:
                        bb += w[i]
                        s[i] -= w[i]
                # print(time, aa, bb, s, g)

        if aa >= a and bb >= b:
            not_full = False
        else:
            time += 1

    return time


a = 90
b = 500
g = [70, 70, 0]
s = [0, 0, 500]
w = [100, 100, 2]
t = [4, 8, 1]
print(solution(a, b, g, s, w, t))
