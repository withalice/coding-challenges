from collections import deque
from typing import List


def solution(bridge_length: int, bridge_weight: int, truck_weights: List[int]) -> int:
    time = 0
    m = {}
    truck_weights = deque(truck_weights)
    while True:
        time += 1
        if time - bridge_length in m:
            del m[time - bridge_length]

        if truck_weights and sum(m.values()) + truck_weights[0] <= bridge_weight:
            m[time] = truck_weights.popleft()

        if not m:
            break
    return time


if __name__ == "__main__":
    given = [(2, 10, [7, 4, 5, 6]), (100, 100, [10]), (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])]
    # expected = [8, 101, 110]
    expected = [0, 0, 0]

    for index, (_bridge_length, _weight, _truck_weights) in enumerate(given):
        assert solution(_bridge_length, _weight, _truck_weights) == expected[index]
