# 단어 섞기
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):

    answer = "no"
    word1, word2, con_word = input().rstrip().split()
    word1 = deque(list(word1))
    word2 = deque(list(word2))
    visit1 = [0 for _ in range(len(word1))]
    visit2 = [0 for _ in range(len(word2))]
    que = deque()
    que.append([word1, word2, visit1, visit2, con_word])
    while que:
        aa, bb, vv1, vv2, ww = que.popleft()

        for idx, word in enumerate(ww):
            if aa:
                a = aa.popleft()
            else:
                a = ""
            if bb:
                b = bb.popleft()
            else:
                b = ""

            if word == a and word == b:
                aaa = deepcopy(aa)
                bbb = deepcopy(bb)
                if a != "":
                    aaa.appendleft(a)
                que.append([aaa, bb, ww[idx + 1 :]])
                # print("B 일치", que)
                if b != "":
                    bbb.appendleft(b)  # a가 일치
                que.append([aa, bbb, ww[idx + 1 :]])
                # print("A 일치", que)
                break
            elif word == a:
                if b != "":

                    bb.appendleft(b)
            elif word == b:
                if a != "":
                    aa.appendleft(a)
            else:
                break

            if idx == len(ww) - 1 and len(aa) == 0 and len(bb) == 0:
                answer = "yes"
    print("Data set " + str(i) + ":", answer)
