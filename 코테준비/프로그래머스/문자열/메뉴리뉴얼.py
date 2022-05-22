import operator
from itertools import combinations


def solution(orders, course):
    answer = []
    order_dict_list = [[] for _ in range(len(course))]

    for i in range(len(course)):
        order_dict = {}
        for order in orders:
            order = list(order)
            order.sort()
            order_list = list(combinations(order, course[i]))

            for k in order_list:
                order_str = "".join(k)
                if order_dict.get(order_str):
                    order_dict[order_str] = order_dict.get(order_str) + 1
                else:
                    order_dict[order_str] = 1
        order_dict_list[i].append(order_dict)

    for i in range(len(order_dict_list)):
        order_dict = sorted(
            order_dict_list[i][0].items(), key=operator.itemgetter(1), reverse=True
        )
        if not order_dict:
            continue
        max = order_dict[0][1]
        if max < 2:
            continue
        else:
            answer.append(order_dict[0][0])
        for j in range(1, len(order_dict)):
            if order_dict[j][1] == max:
                answer.append(order_dict[j][0])

    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 5]
course = [2, 3, 4]
print(solution(orders, course))
