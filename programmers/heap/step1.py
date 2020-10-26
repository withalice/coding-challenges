import heapq


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 1:
        first_value = heapq.heappop(scoville)

        if first_value >= k:
            break
        if len(scoville) < 1:
            return -1
        second_value = heapq.heappop(scoville)
        heapq.heappush(scoville, first_value + (second_value * 2))
        answer += 1

    return answer


if __name__ == "__main__":
    given = [([1, 2, 3, 9, 10, 12], 7)]

    expected = [2]

    for index, (_scoville, _k) in enumerate(given):
        assert solution(_scoville, _k) == expected[index]
