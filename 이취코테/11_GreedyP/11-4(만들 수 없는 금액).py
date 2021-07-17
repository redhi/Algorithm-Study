N = int(input())
coins = list(map(int, input().split(" ")))
min_pay = 1
coins.sort()

for coin in coins:
    if min_pay < coin:
        break
    min_pay += coin # 작은 순으로 더해가면서 지불 금액을 구한다

print(min_pay)
