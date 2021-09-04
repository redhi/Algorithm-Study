s = input()
s = ''.join(char for char in s if char.isalnum())
s = list(s)
print(s)


def reverse(s):  # 새로운 리스트 선언해서 -> 조건과 맞지않음
    print(type(s))
    print(s)
    new_s = []
    for i in range(len(s)):
        new_s.append(s[-(i+1)])
    print(new_s)


reverse(s)

s[:] = s[::-1]  # -1씩 증가시켜 전체배열에 넣기
s.reverse
