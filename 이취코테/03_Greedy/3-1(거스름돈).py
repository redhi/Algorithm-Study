money = [500,100,50,10]

change = int(input())
count = 0


for coin in money:
    count += change//coin # 가장 큰 단위의 동전부터 나눈 값을 더한다.
    change = change%coin # 남은 거스름돈을 기존의 변수에 넣어준다.

print(count)
