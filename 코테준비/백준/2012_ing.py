# 등수 매기기
import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
visit = [0 for _ in range(N + 1)]
predict = []
d = defaultdict(int)
p = [0 for i in range(N + 1)]
for i in range(N):
    num = int(input())
    d[num] += 1
    p[num] += 1
    predict.append(num)
predict.sort()
print(predict, d, p)
# 1 1
# 1 1 1
# 2
# 3

# 5
