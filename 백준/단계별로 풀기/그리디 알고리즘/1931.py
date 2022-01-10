"""
백준 회의실 배정
"""
import sys

input = sys.stdin.readline

N = int(input())

m_list = []
for i in range(N):
    s, e = list(map(int, input().split()))
    m_list.append([s, e])

m_list.sort(key=lambda x: (x[1], x[0]))

count = 1
end = m_list[0][1]
for i in range(len(m_list)):
    if i == 0 or m_list[i][0] < end:
        continue
    else:
        end = m_list[i][1]
        count += 1

print(count)
