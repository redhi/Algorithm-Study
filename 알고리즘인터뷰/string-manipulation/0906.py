from collections import deque


def main():
    MAX = 100001
    n, k = map(int, input().split())
    array = [0] * MAX

    q = deque([n])
    while q:
        catch = q.popleft()
        if catch == k:
            print(array[catch])
            break
        for move in (catch - 1, catch + 1, catch * 3):
            if 0 <= move < MAX and not array[move]:
                array[move] = array[catch] + 1
                print(array[move])
                q.append(move)


if __name__ == "__main__":
    main()
