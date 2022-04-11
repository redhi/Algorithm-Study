def solution(s):
    answer = 0
    s = (
        s.replace("zero", "0")
        .replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )
    s = int(s)
    answer = s
    return answer


s = "one4seveneight"

print(solution(s))
