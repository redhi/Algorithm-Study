import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    basic_min, basic_fee, unit_m, unit_fee = fees
    car_dict = defaultdict(list)
    for i in range(len(records)):
        time, car_num, info = records[i].split(" ")
        h, m = map(int, time.split(":"))
        total_m = h * 60 + m
        if car_dict.get(car_num):
            car_dict[car_num].append(total_m)
        else:
            car_dict[car_num].append(total_m)

    key_list = list(car_dict.keys())
    key_list.sort()

    for key in key_list:
        total_mm = 0
        for i in range(0, len(car_dict[key]), 2):
            if i == len(car_dict[key]) - 1:
                total_mm += 23 * 60 + 59 - car_dict[key][i]
            else:
                total_mm += car_dict[key][i + 1] - car_dict[key][i]

        total_won = 0
        if total_mm > basic_min:
            total_won = (
                basic_fee + math.ceil((total_mm - basic_min) / unit_m) * unit_fee
            )
        else:
            total_won = basic_fee
        answer.append(total_won)
    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fees, records))
