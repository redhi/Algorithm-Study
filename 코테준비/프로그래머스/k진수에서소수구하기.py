import math
from collections import deque


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    que = deque()
    while n > 0:
        left = n % k
        n //= k
        que.appendleft(left)

    que = list(que)
    s = "".join(map(str, que))

    while s.count("00") > 0:
        s = s.replace("00", "0")

    if s[-1] == "0":
        s = s[:-1]
    arr1 = list(map(int, s.split("0")))

    for i in range(len(arr1)):
        if arr1[i] == 1:
            continue
        if is_prime_num(arr1[i]):
            answer += 1

    return answer


n = 437674
# n = 110011
k = 3
n = 524287
n = 6
k = 2
print(solution(n, k))
