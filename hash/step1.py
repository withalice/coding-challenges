import collections


def my_solution(participants, completions):
    participants_map = collections.Counter(participants)

    if len(participants) - len(completions) != 1:
        return

    for completion in completions:
        if completion in participants_map:
            participants_map.update({completion: -1})
            if participants_map.get(completion) == 0:
                participants_map.pop(completion)
    return "".join(participants_map.keys())


def short_solution(participants, completions):
    if len(participants) - len(completions) != 1:
        raise ValueError
    answer = collections.Counter(participants) - collections.Counter(completions)
    return list(answer.keys())[0]


if __name__ == "__main__":
    case_1_par, case_1_com = ["leo", "kiki", "eden"], ["eden", "kiki"]
    case_2_par, case_2_com = ["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]
    case_3_par, case_3_com = ["ana", "ana", "mislav", "stanko", "mislav", "mislav"], ["stanko", "ana", "mislav",
                                                                                      "mislav", "ana"]

    assert my_solution(case_1_par, case_1_com) == "leo"
    assert my_solution(case_2_par, case_2_com) == "vinko"
    assert my_solution(case_3_par, case_3_com) == "mislav"
