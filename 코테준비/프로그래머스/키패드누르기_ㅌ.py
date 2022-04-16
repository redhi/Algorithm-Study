def solution(numbers, hand):
    answer = ""
    left_now, right_now = "*", "#"
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += "L"
            left_now = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += "R"
            right_now = numbers[i]
        else:
            l = numbers[i] - 1
            r = numbers[i] + 1
            u = numbers[i] - 3
            d = numbers[i] + 3
            if numbers[i] == 2:
                u, d = 13, numbers[i] + 3
            elif numbers[i] == 8:
                d = 0
            elif numbers[i] == 0:
                l, r, u, d = "*", "#", 8, 13

            # print("이ㅑㅇ", l, r, u, d)
            if (left_now == l or left_now == r or left_now == u or left_now == d) and (
                right_now == l or right_now == r or right_now == u or right_now == d
            ):
                if hand == "right":
                    answer += "R"
                    right_now = numbers[i]
                else:
                    answer += "L"
                    left_now = numbers[i]
            elif left_now == l or left_now == r or left_now == u or left_now == d:
                answer += "L"
                left_now = numbers[i]
            elif right_now == l or right_now == r or right_now == u or right_now == d:
                right_now = numbers[i]
                answer += "R"
            else:

                l_n, r_n, l_c, r_c = left_now, right_now, 0, 0
                if l_n == 0:
                    l_n = 11
                if r_n == 0:
                    r_n = 11
                if left_now == 1 or left_now == 4 or left_now == 7:
                    l_n += 1
                    l_c += 1
                l_c += abs(l_n - numbers[i]) // 3
                if right_now == 3 or right_now == 6 or right_now == 9:
                    r_n -= 1
                    r_c += 1
                r_c += abs(r_n - numbers[i]) // 3
                # print("카운트", l_c, r_c)
                if l_c == r_c:
                    if hand == "right":
                        answer += "R"
                        right_now = numbers[i]
                    else:
                        answer += "L"
                        left_now = numbers[i]
                elif l_c < r_c:
                    # print("으하하")
                    answer += "L"
                    left_now = numbers[i]
                else:
                    answer += "R"
                    right_now = numbers[i]

        # print(left_now, right_now, numbers[i], answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "right"
hand = "left"
print(solution(numbers, hand))
