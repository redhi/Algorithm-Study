import math

temp = float(input("온도를 입력하세요"))
wind = float(input("풍속(m/s)을 입력하세요"))
wind2 = wind*3600/1000
windchill = 13.12 + 0.6215*temp - 11.37*pow(wind2, 0.16) + 0.3965*temp*pow(wind2,0.16)
result = math.floor(windchill)
print("체감온도는 ", result)
