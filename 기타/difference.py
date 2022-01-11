from collections import deque


def solution(D, X):
    # write your code in Python 3.6
    D = deque(D)

    count = 1
    temp_x = X
    node = D.popleft()
    while D:

        if len(D) == 0:
            break

        if abs(node - D[0]) > temp_x:
            count += 1
            temp_x = X
            node = D[0]
        else:
            temp_x -= abs(node - D[0])
            node = D.popleft()

    return count


print(solution([1, 12, 10, 4, 5, 2, 3, 2, 2], 2))
