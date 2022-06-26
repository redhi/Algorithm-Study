def solution(routes):
    answer = 0

    mm = -300001
    mi = 300001
    for r in routes:
        m = max(r)
        n = min(r)
        mm = max(mm, m)
        mi = min(n, mi)

    arr = [0 for _ in range(mm - mi)]
    for r in routes:
        s = r[0]
        e = r[1]
        for i in range(s, e):
            arr[abs(mi - i)] += 1
            print(i, abs(mi - i))

    answer = len(routes) - max(arr)

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3], [20, 10]]
print(solution(routes))
