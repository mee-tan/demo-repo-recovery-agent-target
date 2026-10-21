import pytest

from calculator.ops import add, divide, multiply, subtract


# test addition using the add method in ops module.
def test_add():
    assert add(2, 3) == 5

# test subtraction using the subtract method in ops module
def test_subtract():
    assert subtract(5, 3) == 2

# test multiplication using the multiply method in ops module
def test_multiply():
    assert multiply(4, 3) == 12

# test division using the divide method in ops module
def test_divide():
    assert divide(10, 2) == 5

# test division by zero
def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)