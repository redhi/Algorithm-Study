import math
from collections import deque


def solution(fees, records):
    answer = []
    basic_min = fees[0]
    basic_fee = fees[1]
    unit_min = fees[2]
    unit_fee = fees[3]
    car_record = [[] for i in range(len(records))]
    car_num_list = []
    for i in range(len(records)):
        record = records[i].split()
        car_num = record[1]
        time = record[0].split(":")
        time_min = int(time[0]) * 60 + int(time[1])
        in_or_out = record[2]
        car_record[i].extend([car_num, time_min, in_or_out])
        car_num_list.append(car_num)
    car_num_list.sort()
    car_record.sort(key=lambda x: (x[0], x[1]))

    que = deque()

    que.append([car_num_list[0], 0])

    while que:
        car_num1, idx = que.popleft()
        same_car = car_num_list.count(car_num1)
        pay_fee = 0
        total_min = 0
        for i in range(idx, same_car + idx, 2):

            (
                car_num2,
                time_min,
                in_or_out,
            ) = car_record[i]
            if i == same_car + idx - 1:

                total_min += 23 * 60 + 59 - time_min
            else:
                (
                    car_num3,
                    time_min2,
                    in_or_out2,
                ) = car_record[i + 1]
                # print(i, "엥???")
                total_min += time_min2 - time_min
        # print("총 분수", total_min)

        if total_min <= basic_min:
            pay_fee = basic_fee
        else:
            pay_fee = (
                math.ceil(((total_min - basic_min) / unit_min)) * unit_fee + basic_fee
            )
        answer.append(pay_fee)
        if same_car + idx != len(car_record):
            que.append([car_num_list[same_car + idx], same_car + idx])

    # print(car_record)

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
