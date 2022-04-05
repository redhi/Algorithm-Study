from audioop import reverse


def solution(nodeinfo):
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    print(nodeinfo)
    tree = [[] for _ in range(len(nodeinfo))]
    degree = []
    for i in range(len(nodeinfo)):
        tree_info = []
        minus_value = 0
        for j in range(i, len(nodeinfo)):
            if nodeinfo[i][1] != nodeinfo[j][1]:
                break
            tree_info.append(nodeinfo[j])
        degree.append(tree_info)

    print(degree)
    for i in range(len(nodeinfo)):
        tree_info = [nodeinfo[i][2], 0, 0]
        minus_value = 0
        for j in range(i, len(nodeinfo)):
            if nodeinfo[i][1] != nodeinfo[j][1]:
                if minus_value == 0:
                    minus_value = nodeinfo[i][1] - nodeinfo[j][1]
                    print(minus_value)
                else:
                    minus_value2 = nodeinfo[i][1] - nodeinfo[j][1]
                    print(nodeinfo[i][1], nodeinfo[j][1])
                    if minus_value != minus_value2:
                        print(i, j, "나옴")
                        break

                print("으아", nodeinfo[j][2], nodeinfo[i][2])
                if nodeinfo[j][0] < nodeinfo[i][0]:
                    tree_info[1] = nodeinfo[j][2]
                else:
                    tree_info[2] = nodeinfo[j][2]
        tree[i].append(tree_info)
    print(tree)

    return answer


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(nodeinfo))
