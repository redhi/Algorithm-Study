# 교환학생
TC = int(input())
for i in range(1, TC + 1):
    n = int(input())
    day = list(map(int, input().split()))
    day_num = day.count(1)
    answer = ((n // day_num) - 1) * 7

    left = n % day_num
    count = 0
    if left == 0:
        answer += 1
    else:
        answer += 7
        for j in range(7):
            if day[j] == 1:
                count += 1
            if count == left:
                answer += j + 1
                break

    print("#" + str(i), answer)
