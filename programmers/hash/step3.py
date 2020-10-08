import collections


def my_solution(clothes):
    answer = 1
    clothes_map = collections.Counter([kind for name, kind in clothes])

    value_list = list(clothes_map.values())

    for i in range(len(value_list)):
        answer *= value_list[i] + 1
    return answer - 1


if __name__ == "__main__":
    case_9 = [["", "headgear"]]
    case_1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    case_2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    case_3 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellow_hat", "headgear"],
              ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    assert my_solution(case_1) == 5
    assert my_solution(case_2) == 3
    assert my_solution(case_3) == 23
