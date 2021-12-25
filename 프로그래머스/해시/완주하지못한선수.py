"""
프로그래머스 완주하지 못한 선수
"""


def solution(participant, completion):
    dic = dict()
    hashValue = 0

    for i in participant:
        # 해시를 이용해 키값으로 지정
        dic[hash(i)] = i
        hashValue += hash(i)

    for j in completion:
        # 완주한 선수들 제거
        hashValue -= hash(j)

    return dic[hashValue]
