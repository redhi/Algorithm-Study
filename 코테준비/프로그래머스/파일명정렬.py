def solution(files):
    answer = []
    file_info = []
    for i in range(len(files)):
        digit_start = 0
        tail_start = 0
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                digit_start = j
                break
        for j in range(j, len(files[i])):
            if (
                files[i][j].isalpha()
                or files[i][j] == "."
                or files[i][j] == " "
                or files[i][j] == "-"
            ):
                tail_start = j
                break
        if tail_start == 0:
            tail_start = len(files[i])

        head = files[i][:digit_start]
        number = files[i][digit_start:tail_start]
        tail = files[i][tail_start:]
        file_info.append([head.lower(), int(number), tail, i])

    file_info.sort(key=lambda x: (x[0], x[1], x[3]))

    for i in range(len(file_info)):
        idx = file_info[i][3]
        answer.append(files[idx])
    return answer


files = ["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = [
#     "F-5 Freedom Fighter",
#     "B-50 Superfortress",
#     "A-10 Thunderbolt II",
#     "F-14 Tomcat",
# ]
print(solution(files))
