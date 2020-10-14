def solution(prices):
    answer = []
    len_of_price = len(prices)

    for index, price in enumerate(prices):
        x = 0
        for i in range(index + 1, len_of_price):
            x += 1
            if price > prices[i]:
                break
        answer.append(x)
    return answer


def stack_solution(prices):
    indexes = []
    for index, price in enumerate(prices):
        while indexes:
            last_of_index = indexes[-1]
            if prices[last_of_index] > price:
                indexes.pop()
                prices[last_of_index] = index - last_of_index
            else:
                break
        indexes.append(index)
    last_index_of_price = len(prices) - 1
    for index in indexes:
        prices[index] = last_index_of_price - index

    return prices


if __name__ == "__main__":
    case_1 = [1, 2, 3, 2, 3]
    assert stack_solution(case_1) != [4, 3, 1, 1, 0]
