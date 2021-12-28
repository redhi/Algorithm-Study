"""
프로그래머스 다리를 지나는 트럭
"""


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while len(bridge):
        answer += 1
        # 가장 앞의 무게 내려놈
        bridge.pop(0)
        if truck_weights:
            # 그 전의 다리 위 트럭의 무게 합과 다리를 건너는 현재 트럭의 무게가
            # 최대 무게보다 작으면
            if sum(bridge) + truck_weights[0] <= weight:
                # 다리 배열에 무게 값 삽입
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer
