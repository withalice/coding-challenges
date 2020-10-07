def my_solution(phone_books):
    phone_books = sorted(set(phone_books))
    count_of_books = len(phone_books)
    for i in range(count_of_books - 1):

        if phone_books[i + 1].startswith(phone_books[i]):
            return False
    return True


if __name__ == "__main__":
    case_1 = ["119", "97674223", "1195524421"]
    case_2 = ["123", "456", "789"]
    case_3 = ["12", "123", "1235", "567", "88"]
    case_4 = ["8894", "1235", "567", "88"]
    assert my_solution(case_1) is False
    assert my_solution(case_2) is True
    assert my_solution(case_3) is False
    assert my_solution(case_4) is False
