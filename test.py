import pytest

def test_my_funktion():
    sum_result, dele_result, dobytok_result, dilenya_result = my_funktion(3, 3)

    assert sum_result == 6
    assert dele_result == 0
    assert dobytok_result == 9
    assert dilenya_result == 1






def test_no_zero():

    assert no_zero(5) == 5

    with pytest.raises(ValueError):
        no_zero(-1)




def test_palindrome():
    assert palindrome("Мадам")
    assert palindrome("Анна")
    assert palindrome("Привіт")
