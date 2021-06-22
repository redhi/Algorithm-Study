city = int(input())
length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
min_price = oil_price[0]
result = 0

for i in range(len(length)):
    if oil_price[i] >= min_price:
        result += min_price * length[i]
    elif oil_price[i] < min_price:
        min_price = oil_price[i]
        result += min_price * length[i]
        
print(result)
