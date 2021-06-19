N = int(input())
count = 0
my_stack = []
result = []
msg = True

for i in range(N):
    x = int(input())

    while count < x:
      count += 1
      my_stack.append(count)
      result.append("+")

    if my_stack[-1]==x:
        my_stack.pop()
        result.append("-")
    else:
        msg = False
        break

if msg==False:
    print("NO")
else:
    print("\n".join(result))
