'''04 가장 흔한 단어
leetcode 819. Most Common Word
https://dojang.io/mod/page/view.php?id=2438'''
import re
paragraph = input()

banned = input()

# 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 반환
# lower는 list에 적용 불가 순서가 중요


def common(paragraph, banned):
    words = [w for w in re.sub(
        r'[^\w]', ' ', paragraph).lower().split() if w not in banned]

    new = {}
    for word in words:  # 딕셔너리로 빈도수 분류
        if word in new:
            new[word] += 1
        else:
            new[word] = 1

    for i in new:  # 키 값으로 출력됨, 최대 출력
        if new[i] == max(new.values()):
            print(i)


common(paragraph, banned)
#common("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
