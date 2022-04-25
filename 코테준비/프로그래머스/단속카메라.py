def solution(routes):
    answer = 0
    # print(max(routes))
    mm = -300001
    mi = 300001
    for r in routes:
        m = max(r)
        n = min(r)
        # print(m, n)
        mm = max(mm, m)
        mi = min(n, mi)
    # -20 -3
    # 23
    # -3 -(-3)
    # -20 -(-3)

    # print(mm, mi)
    arr = [0 for _ in range(mm - mi)]
    # print(len(arr))
    for r in routes:
        s = r[0]
        e = r[1]
        for i in range(s, e):
            arr[abs(mi - i)] += 1
            print(i, abs(mi - i))
    print(arr)
    answer = len(routes) - max(arr)

    # arr[abs()]

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3], [20, 10]]
print(solution(routes))
