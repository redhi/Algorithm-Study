from bisect import bisect_left


def solution(n, k, cmd):
    answer = ""
    arr = [0] * (n)
    stack = []
    count = 0
    for i in cmd:
        c = i.split(" ")
        if c[0] == "D":
            cc = int(c[1])
            ss = sorted(stack)
            ss = [0, 1, 4, 6]
            print(ss)
            idx = bisect_left(ss, k)
            cc -= ss[idx] - k + 1
            for i in range(idx+1, len(ss)):
                if ss[i-1]
                

            print()
            print(stack, cc, "현재", k)
            # k += cc +
            while cc > 0:
                k += 1
                if k == n:
                    k = n - 1
                    break
                if arr[k] == 0:
                    cc -= 1

        if c[0] == "U":
            cc = int(c[1])
            while cc > 0:
                k -= 1
                if k < 0:
                    k = 0
                    break
                if arr[k] == 0:
                    cc -= 1

        if c[0] == "C":
            arr[k] = 1
            stack.append(k)
            # count += 1

            if k == n - 1:
                k -= 1
            else:
                k += 1

        if c[0] == "Z":
            # count -= 1
            num = stack.pop()
            arr[num] = 0
        print(k, arr, count)

    for i in range(len(arr)):
        if arr[i] == 0:
            answer += "O"
        else:
            answer += "X"
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# cmd = ["D 2", "C", "Z", "U 3", "C", "Z", "C"]
print(solution(n, k, cmd))
