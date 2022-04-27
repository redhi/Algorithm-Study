def solution(numbers, hand):
    answer = ""
    left = [3, 0]
    right = [3, 2]
    left_list = [1, 4, 7]
    right_list = [3, 6, 9]
    middle_list = [2, 5, 8, 0]

    for number in numbers:
        l_y, l_x = left
        r_y, r_x = right
        if number in left_list:
            y = left_list.index(number)
            x = 0
            left = [y, x]
            answer += "L"
        elif number in right_list:
            y = right_list.index(number)
            x = 2
            right = [y, x]
            answer += "R"
        else:
            x = 1
            y = middle_list.index(number)

            right_count = abs(r_y - y) + abs(r_x - x)
            left_count = abs(l_y - y) + abs(l_x - x)

            if left_count > right_count:
                answer += "R"
                right = [y, x]
            elif left_count < right_count:
                answer += "L"
                left = [y, x]
            else:
                if hand == "left":
                    answer += "L"
                    left = [y, x]
                else:
                    answer += "R"
                    right = [y, x]

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "right"
hand = "left"
print(solution(numbers, hand))
