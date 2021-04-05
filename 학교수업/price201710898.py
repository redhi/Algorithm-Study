carval = 10
oil = 1400
aver = 40
money = 8720
A_km = float(input("쇼핑몰 A까지의 거리를 km단위로 입력하세요:"))
A_price = float(input("쇼핑몰 A의 컴퓨터 가격을 입력하세요:"))
A_total = (A_km*2)/carval*oil + (A_km*2)/aver*money + A_price
print("쇼핑몰 A에서 구입하는 전체 비용은 ",A_total,"입니다.")
B_km = float(input("쇼핑몰 B까지의 거리를 km단위로 입력하세요:"))
B_price = float(input("쇼핑몰 B의 컴퓨터 가격을 입력하세요:"))
B_total = (B_km*2)/carval*oil + (B_km*2)/aver*money + B_price
print("쇼핑몰 B에서 구입하는 전체 비용은 ",B_total,"입니다.")
if(A_total>B_total):
    print("쇼핑몰 B에서 구입하는 것이 좋습니다")
else:
    print("쇼핑몰 A에서 구입하는 것이 좋습니다")
