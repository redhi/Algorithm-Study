"""
프로그래머스 전화번호 목록
zip, startswith 사용
"""


def solution(phone_book):
    # 접두사에 포함되어 표현하도록 정렬
    phone_book.sort()
    
    # 그 현재와 다음 번호 추출
    for p1, p2 in zip(phone_book, phone_book[1:]):
        # p2에 p1의 번호로 시작하면
        if p2.startswith(p1):
            return False

    return True
