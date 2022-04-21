def solution(n, k, cmd):
    answer = ""
    arr = [0] * (n)
    stack = []
    for i in cmd:
        c = i.split(" ")
        if c[0] == "D":
            cc = int(c[1])
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

            if k == n - 1:
                k -= 1
            else:
                k += 1

        if c[0] == "Z":
            num = stack.pop()
            arr[num] = 0

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
