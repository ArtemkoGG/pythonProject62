import pytest
def no_zero(number):
    if number < 0:
        raise ValueError
    return number

no_zero()
test_no_zero()