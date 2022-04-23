def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    # print(costs)
    p = [i for i in range(n)]

    def find_parent(node):
        if p[node] == node:
            return p[node]
        else:
            return find_parent(p[node])

    def union(a, b):
        p_a = find_parent(a)
        p_b = find_parent(b)
        if p_a != p_b:
            p[p_b] = p_a

    for cost in costs:
        a, b, v = cost
        if find_parent(a) != find_parent(b):
            union(a, b)
            answer += v
            # print(p)
    return answer


n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, costs))
