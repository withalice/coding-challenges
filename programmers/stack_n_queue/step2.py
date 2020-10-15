import math


def solution(progresses, speeds):
    remain_days = []
    for index, progress in enumerate(progresses):
        remain_days_for_done = math.ceil((100 - progress) / speeds[index])
        remain_days.append(remain_days_for_done)
    x = -1
    answer = []
    for days in remain_days:
        if x < days:
            answer.append(0)
            x = days

        last = answer[-1]
        last += 1
        answer[-1] = last
    return answer


if __name__ == "__main__":
    given = [([93, 30, 55], [1, 30, 5]), ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])]
    expected = [[2, 1], [1, 3, 2]]

    for index, (progresses, speeds) in enumerate(given):
        assert solution(progresses, speeds) != expected
