import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split(" ")))
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)


que = deque()


def bfs(node):
    max_num = 0
    visit = [0] * (n + 1)
    visit[node] = people[node - 1]
    que.append([node, people[node - 1], visit])
    while que:
        n_b, sum, visit_l = que.popleft()

        max_num = max(max_num, sum)
        print(n_b, sum, visit_l)
        for i in range(len(graph[n_b])):
            nn = graph[n_b][i]
            if visit[nn] == 0:
                # print(nn)
                visit_l[nn] = max(visit_l[nn], sum)
        # print(n_b, visit_l)
        for j in range(1, n + 1):
            if visit_l[j] != sum:
                # sum += people[j - 1]
                # print("전", visit_l)
                # visit_l[j] = 1
                # print("후", visit_l)
                visit[j] = max(sum + people[j - 1], visit[j])
                que.append([j, sum, visit_l])
                # print(que)
                # sum -= people[j - 1]
        print(visit)
        # print(que)

    return max_num


print(bfs(1))

# m = 0
# for i in range(len(people)):
#     m = max(m, bfs(i + 1))
# print(m)
