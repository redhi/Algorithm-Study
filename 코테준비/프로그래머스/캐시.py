from collections import deque


def solution(cacheSize, cities):
    answer = 0
    que = deque()

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for i in range(len(cities)):
            city = cities[i].lower()

            if len(que) < cacheSize:
                if city in que:
                    que.remove(city)
                    que.append(city)
                    answer += 1
                else:
                    answer += 5
                    que.append(city)
            else:
                if city in que:
                    que.remove(city)
                    que.append(city)
                    answer += 1
                else:
                    answer += 5
                    que.popleft()
                    que.append(city)
    return answer


cacheSize = 3
cacheSize = 4
# cacheSize = 5
# cacheSize = 1
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
]
# cities = ["newyork", "Jeju", "Pangyo", "NewYork"]
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "jeju",
    "NewYork",
    "LA",
    "SanFrancisco",
    "jeju",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
]
# cities = [
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "Jeju",
#     "Pangyo",
#     "Seoul",
# ]
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))
