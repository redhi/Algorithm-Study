N = int(input())
fear_arr = list(map(int, input().split(" ")))

new_arr = []  # 공포도에 맞는 인원수를 측정하기 위한 배열
count = 0
fear_arr.sort(reverse=True)  # 배열 정렬(공포도 높은 순)

for i in range(N):
    new_arr.append(fear_arr[i])

    if new_arr[0] == len(new_arr):  # new_arr에 새로 들어간 첫번째와 길이 비교
        new_arr.clear()  # 조건 충족 후 리스트 전체삭제
        count += 1  # 집단 수 증가

print(count)
