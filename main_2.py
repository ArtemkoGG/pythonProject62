import pytest
def upper(s):
    return s.upper()

def test_upper():
    assert upper("привіт") == "ПРИВІТ"

def palindrome(s):
    return s == s[::-1]


upper("привіт")
test_upper()
palindrome()
test_palindrome()